"""
@author: cunyue
@file: __init__.py
@time: 2026/3/5 14:38
@description: SwanLab 包配置项，根据优先级从低到高加载配置：
1. 默认值
2. settings.root
3. 环境变量
4. 当前目录下 .env 文件
5. /etc/swanlab/*.{yaml,yml}
6. 当前目录下 swanlab.{yaml,yml}
7. K8S/Docker 容器 Secret 配置项文件

在设计上 Settings 仅是与用户交互的配置入口，不包含业务逻辑，这意味着仅检查必要的类型和格式和必要的默认值，不产生副作用：
1. 文件夹创建
2. 具体业务逻辑，如实验id生成与格式校验、实验名称长度校验等

用户可以通过merge_settings动态合并配置，但是在设计上，在执行`swanlab.init`和`swanlab.finish`之间，无法使用merge_settings。
"""

import os
from pathlib import Path
from typing import Any, ClassVar, Dict, Optional, Tuple, Type, Union, get_args

from pydantic import Field, field_validator
from pydantic.functional_validators import model_validator
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SecretsSettingsSource,
    SettingsConfigDict,
    YamlConfigSettingsSource,
)

from swanlab.sdk.internal.pkg import helper, nrc, safe
from swanlab.sdk.typings.run import ModeType

from .experiment import ExperimentSettings, ProjectSettings, RunSettings
from .integration import IntegrationSettings
from .metadata import ConsoleSettings, EnvironmentSettings, MonitorSettings

__all__ = ["Settings", "settings", "ROOT_FOLDER"]


# 根据环境变量自动设置 secrets_dir
# 如果强制设置，会出现警告：https://github.com/pydantic/pydantic/issues/2175
secrets_dir_env = os.getenv("SWANLAB_SECRETS_DIR")
SECRETS_DIR: Optional[str] = secrets_dir_env or None

# 根据环境变量选择全局配置文件路径
config_dir_env = os.getenv("SWANLAB_CONFIG_DIR")
ROOT_FOLDER = ".swanlab"
CONFIG_DIR: str = config_dir_env or "/etc/swanlab"


def root_factory() -> Path:
    # 向下兼容旧版本环境变量
    return Path.home() / ROOT_FOLDER


def log_dir_factory() -> Path:
    return Path.home() / ROOT_FOLDER / "logs"


class Settings(BaseSettings):
    """SwanLab configuration settings.

    This class manages all SwanLab configuration options, loaded from multiple sources
    in order of priority: defaults → environment variables → config files → user code.

    Use `swanlab.merge_settings()` to customize settings before calling `swanlab.init()`.

    Examples:

        Create custom settings:

        >>> from swanlab import Settings
        >>> settings = Settings(mode="local", logdir="./my_logs")
        >>> import swanlab
        >>> swanlab.merge_settings(settings)
        >>> run = swanlab.init()

        Configure nested settings:

        >>> from swanlab import Settings
        >>> settings = Settings(
        ...     mode="cloud",
        ...     monitor=Settings.Monitor(enable=False)
        ... )
        >>> import swanlab
        >>> swanlab.merge_settings(settings)
    """

    Project: ClassVar[Type[ProjectSettings]] = ProjectSettings
    Run: ClassVar[Type[RunSettings]] = RunSettings
    Experiment: ClassVar[Type[ExperimentSettings]] = ExperimentSettings
    Metadata: ClassVar[Type[EnvironmentSettings]] = EnvironmentSettings
    Monitor: ClassVar[Type[MonitorSettings]] = MonitorSettings
    Console: ClassVar[Type[ConsoleSettings]] = ConsoleSettings
    Integration: ClassVar[Type[IntegrationSettings]] = IntegrationSettings

    interactive: bool = True
    """
    Whether to enable interactive mode.
    If False, all user input prompts and related interactions will be disabled.
    Useful for CI/CD environments or background batch jobs.
    """

    mode: ModeType = "cloud"
    """
    SwanLab Run mode.

    * `local`: Run SwanLab locally.
    * `cloud`: Run SwanLab on the cloud.
    * `disabled`: Disable SwanLab.
    * `offline`: Run SwanLab in offline mode.
    """

    @field_validator("mode", mode="before")
    def validate_mode(cls, v: Any) -> ModeType:
        return v

    root: Path = Field(default_factory=root_factory)
    """
    Directory for SwanLab saved files.
    """

    @field_validator("root", mode="before")
    def validate_root(cls, v: Union[str, Path]) -> Path:
        """
        如果 root 存在，必须是目录
        """
        return Path(v) if v is not None else root_factory()

    log_dir: Path = Field(default_factory=log_dir_factory, validate_default=True)
    """
    Directory for SwanLab logs.
    Semantically, this is just a path representation and the directory may NOT exist when loaded. 
    The actual folder creation is deferred to the SDK initialization phase to avoid side effects.
    """

    @field_validator("log_dir", mode="before")
    def validate_log_dir(cls, v: Union[str, Path]) -> Path:
        """
        如果 log_dir 存在，必须是目录
        """
        return Path(v) if v is not None else log_dir_factory()

    api_key: Optional[str] = Field(default=None)
    """
    API key for SwanLab services.
    """
    api_host: str = Field(default="https://api.swanlab.cn")
    """
    Base URL for SwanLab API services.
    """
    web_host: str = Field(default="https://swanlab.cn")
    """
    Base URL for SwanLab web services.
    It just a display URL for SwanLab web services, no actual effect on SDK behavior.
    """

    @model_validator(mode="before")
    @classmethod
    def strip_non_empty(cls, data: Dict) -> Dict:
        """
        删除空值和空字典，以适配传入None的情况，一般情况下此校验必须在其他model_validator之前定义
        如果出现部分字段需要识别None值，则在此校验之前定义model_validator
        """
        return data if isinstance(data, dict) else {}

    @model_validator(mode="before")
    @classmethod
    def validate_hosts(cls, data: Dict) -> Dict:
        """
        校验并清理 HOST 字段，确保它们以正确的格式存在
        在设计上，api_host 是最基础URL，但是有时候展示的前端URL和后端URL可能不一致
        所以在处理时，我们优先使用 api_host，然后根据需要（当没有显式配置 web_host 时）推导 web_host
        """
        return data if isinstance(data, dict) else {}

    @model_validator(mode="after")
    def load_api_key(self) -> "Settings":
        """
        在所有配置加载完成后，作为最后的回退机制读取 本地 .netrc 文件。
        参考git的设计，.netrc 文件的读取规则为：

        1. 先读取 pwd / .swanlab / .netrc，作为项目级别的swanlab认证信息
        2. 如果项目级别没有，再读取用户主目录下的 .netrc，作为全局级别的认证信息

        只会覆盖未被显式设置（如环境变量/YAML）的默认配置。

        映射规则：
        - machine (host) -> api_host
        - login (username) -> web_host
        - password -> api_key
        """
        return self

    project: ProjectSettings = Field(default_factory=ProjectSettings)
    """
    Configuration for the project of this SwanLab run.
    """
    experiment: ExperimentSettings = Field(default_factory=ExperimentSettings)
    """
    Configuration for the experiment of this SwanLab run.
    """
    run: RunSettings = Field(default_factory=RunSettings)
    """
    Configuration for the run of this SwanLab experiment.
    """
    environment: EnvironmentSettings = Field(default_factory=EnvironmentSettings)
    """
    Configuration for one-time system snapshot collection (hardware specs, runtime, Python env, git, etc.).
    """
    monitor: MonitorSettings = Field(default_factory=MonitorSettings)
    """
    Configuration for periodic hardware monitoring (CPU, GPU, memory, disk I/O, etc.).
    """
    console: ConsoleSettings = Field(default_factory=ConsoleSettings)
    """
    Configuration for SwanLab terminal log collection.
    """
    integration: IntegrationSettings = Field(default_factory=IntegrationSettings)
    """
    Configuration for SwanLab integrations, including webhook, dashboard, etc.
    """

    model_config = SettingsConfigDict(
        env_prefix="SWANLAB_",
        env_nested_delimiter="_",
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_max_split=1,
        extra="ignore",
        frozen=True,
        # 指定 Secret 文件存放目录，通常在容器中挂载到这里
        secrets_dir=SECRETS_DIR,
        validate_assignment=True,
        str_strip_whitespace=True,
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:

        # 优先级由高到低排列体现在返回的sources顺序：
        # 1. init_settings (merge_settings 传入的参数)
        # 2. 当前目录下 swanlab.yaml
        # 3. /etc/swanlab/*.yaml
        # 4. .env 文件
        # 5. file_secret_settings (容器 Secrets)
        # 6. env_settings (环境变量)
        # 7. 默认值 (Model Default)
        return (init_settings,)

    def merge_settings(self, other: Union["Settings", dict]) -> None:
        """
        合并自定义设置
        """
        if isinstance(other, self.__class__):
            # 1. 使用 exclude_unset=True 提取用户显式设置的字段
            # 这样可以确保 SwanLabSettings("log_dir"="...") 不会带上默认的值
            update_data = other.model_dump(exclude_unset=True)
        elif isinstance(other, dict):
            update_data = other
        else:
            raise TypeError(f"Only {self.__class__.__name__} or dict can be merged, not {type(other)}")

        # 2. 获取当前实例的完整状态字典
        current_data = self.model_dump()

        # 3. 递归合并数据 (确保嵌套的 dict 如 collect.metadata 不会被整个替换)
        merged_data = _deep_update(current_data, update_data)

        # 4. 验证新数据：通过类构造函数生成临时实例以触发校验和 Path 转换
        # 这一步能确保传入的路径字符串被 field_validator 处理成 Path 对象并创建目录
        validated_instance = self.__class__(**merged_data)

        # 5. 更新当前单例
        for field_name in self.__class__.model_fields.keys():
            new_value = getattr(validated_instance, field_name)
            # 绕过 frozen=True 的限制
            object.__setattr__(self, field_name, new_value)

        # 由于我们 绕过了 frozen=True 的限制，需要手动同步 __pydantic_fields_set__
        object.__setattr__(self, "__pydantic_fields_set__", validated_instance.__pydantic_fields_set__)


def _deep_update(base_dict: dict, update_dict: dict) -> dict:
    """递归合并字典，用于嵌套模型的 merge_settings"""
    for k, v in update_dict.items():
        if k in base_dict and isinstance(base_dict[k], dict) and isinstance(v, dict):
            base_dict[k] = _deep_update(base_dict[k], v)
        else:
            base_dict[k] = v
    return base_dict


def _load_netrc(netrc_path: Path) -> Optional[Tuple[str, str, str]]:
    pass


settings = Settings()
