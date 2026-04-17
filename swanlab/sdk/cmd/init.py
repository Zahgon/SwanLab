"""
@author: cunyue
@file: init.py
@time: 2026/3/6 21:47
@description: SwanLab SDK 初始化方法
我们在设计上将init前后作为分界线，在init之前出现的错误（如登录失败）被视为critical错误，一旦报错直接退出（大多数情况下）
在init之后的swanlab内部错误被视为non-critical错误，会尝试继续运行，但会记录错误日志
init函数执行时被视为init之前
"""

import json
import os
from datetime import datetime
from functools import partial
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

import requests
import yaml

from swanlab.sdk.cmd.guard import with_cmd_lock
from swanlab.sdk.internal.context import (
    RunConfig,
    RunContext,
    callbacker,
    use_context,
)
from swanlab.sdk.internal.core_python import client
from swanlab.sdk.internal.core_python.api.project import get_or_create_project, get_project
from swanlab.sdk.internal.pkg import console, fs, helper, safe
from swanlab.sdk.protocol import Callback
from swanlab.utils import generate_color, generate_id, generate_name

from ..internal.core_python.api.experiment import create_or_resume_experiment
from ..internal.run import Run, get_run, has_run
from ..internal.settings import Settings
from ..internal.settings import settings as global_settings
from ..typings.run import ModeType, ResumeType
from . import utils
from .login import login_cli, login_raw

__all__ = ["init", "ConfigLike"]


def set_nested_value(d: dict, key: str, value: Any):
    """
    根据点分隔的键路径设置嵌套字典中的值
    例如: set_nested_value(d, "a.b.c", 1) 会设置 d["a"]["b"]["c"] = 1
    注意: 如果 value 为 None，则不会设置该值
    :param d: 要操作的字典
    :param key: 键路径，使用点分隔
    :param value: 要设置的值，如果为 None 则不设置
    """
    pass


def compatible_kwargs(model_dict: dict, **kwargs) -> dict:
    """
    由于不同库的参数名不同，并且照顾到用户习惯，我们需要针对一些参数进行兼容性处理。
    将一些额外的参数合并到 model_dict 中
    """
    # experiment_name --> name
    pass


ConfigLike = Union[Dict[str, Any], str, os.PathLike]


@with_cmd_lock
def init(
    *,
    reinit: Optional[bool] = None,
    logdir: Optional[str] = None,
    mode: Optional[ModeType] = None,
    workspace: Optional[str] = None,
    project: Optional[str] = None,
    public: Optional[bool] = None,
    name: Optional[str] = None,
    color: Optional[str] = None,
    description: Optional[str] = None,
    job_type: Optional[str] = None,
    group: Optional[str] = None,
    tags: Optional[List[str]] = None,
    id: Optional[str] = None,
    resume: Optional[Union[ResumeType, bool]] = None,
    config: Optional[ConfigLike] = None,
    settings: Optional[Settings] = None,
    callbacks: Optional[List[Callback]] = None,
    **kwargs,
) -> Run:
    """Initialize a new SwanLab run to track experiments.

    This function starts a new run for logging metrics, artifacts, and metadata.
    After calling this, use `swanlab.log()` to log data and `swanlab.finish()` to
    close the run. SwanLab automatically finishes runs at program exit.

    :param reinit: If True, finish the current run before starting a new one. Defaults to False.

    :param logdir: Directory to store logs. Defaults to "./swanlog".

    :param mode: Run mode. Options: "cloud" (sync to cloud), "local" (local only),
        "offline" (save locally for later sync), "disabled" (no logging). Defaults to "cloud".

    :param workspace: Workspace or organization name. Defaults to current user.

    :param project: Project name. Defaults to current directory name.

    :param public: Make project publicly visible (cloud mode only). Defaults to False.

    :param name: Experiment name. Auto-generated if not provided.

    :param color: Experiment color for visualization. Auto-generated if not provided.

    :param description: Experiment description.

    :param job_type: Job type label (e.g., "train", "eval").

    :param group: Group name for organizing related experiments.

    :param tags: List of tags for categorizing experiments.

    :param id: Run ID for resuming a previous run (cloud mode only).

    :param resume: Resume behavior. Options: "must" (must resume), "allow" (resume if exists),
        "never" (always create new). Defaults to "never".

    :param config: Experiment configuration dict or path to config file (JSON/YAML).

    :param settings: Custom Settings object for advanced configuration.

    :param callbacks: List of callback functions triggered on run events.

    :return: The initialized Run object.

    :raises RuntimeError: If a run is already active and reinit=False.

    Examples:

        Basic local run:

        >>> import swanlab
        >>> swanlab.init(mode="local", project="my_project")
        >>> swanlab.log({"loss": 0.5})
        >>> swanlab.finish()

        Cloud run with configuration:

        >>> import swanlab
        >>> swanlab.login(api_key="your_key")
        >>> swanlab.init(
        ...     mode="cloud",
        ...     project="image_classification",
        ...     name="resnet50_experiment",
        ...     config={"lr": 0.001, "batch_size": 32}
        ... )
        >>> swanlab.log({"accuracy": 0.95})
        >>> swanlab.finish()

        Resume a previous run:

        >>> import swanlab
        >>> swanlab.init(
        ...     mode="cloud",
        ...     project="my_project",
        ...     id="previous_run_id",
        ...     resume="must"
        ... )
    """
    pass


def _init(run_settings: Settings) -> RunContext:
    """
    初始化运行时配置，在这之前，所有引导式交互都已经完成
    上下文生命周期通过 `Run` 管理，而非全局 `ContextVar`
    """
    pass


@utils.with_loading_animation()
def _init_cloud(ctx: RunContext, run_id: str):
    """
    在云模式下初始化运行上下文。
    :param ctx: 运行上下文
    :param run_id: 当前运行的唯一标识符
    """
    pass


def load_config(run_settings: Settings, config: Optional[ConfigLike]) -> Dict[str, Any]:
    """
    优雅地加载配置：支持字典直接返回，或从 JSON/YAML 文件加载。
    """
    pass


def _mkdirs(ctx: RunContext):
    """
    创建运行所需的目录
    :param ctx: 运行上下文
    """
    # 对于 logdir 而言，如果不存在则创建，如果为空则写入 .gitignore
    pass


def prompt_init_mode(settings: Settings) -> ModeType:
    """
    在 swanlab.init 阶段，针对 cloud 模式且未登录的用户进行交互式引导。

    规则：
    1. 只有在 settings.interactive 为 True 且 settings.mode 为 'cloud' 时触发 。
    2. 如果 client 已存在（已登录），直接跳过 。
    3. 提供三个选项：(1) 使用已有的Key (2) 注册 (3) 切换为 offline 模式。

    :param settings: 当前的 Settings 实例 。
    :return: 最终确定的 mode
    """
    # 如果不是云模式，或者已经登录，或者非交互环境，直接返回当前状态
    pass


@safe.decorator(message="Failed to send webhook")
def send_webhook(ctx: RunContext) -> Tuple[bool, bool]:
    """
    发送 webhook 回调，仅在非 disabled 模式下触发。

    请求体结构 (JSON):
    {
      "value": "string",  // 即 SWANLAB_WEBHOOK_VALUE 的值
      "swanlab": {
        "version": "string",     // swanlab 版本号
        "mode": "cloud" | "local", // swanlab 运行模式
        "run_dir": "string",  // 日志存储路径
        "exp_url": "string"       // 云端实验路径
      }
    }

    :param ctx: 运行上下文
    :return: (是否发送，是否成功)
    """
    pass
