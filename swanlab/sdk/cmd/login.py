"""
@author: cunyue
@file: login.py
@time: 2026/3/6 22:24
@description: swanlab.login 方法，登录到 SwanLab 平台
"""

import getpass
import sys
from pathlib import Path
from typing import Optional

from rich.text import Text

from swanlab.exceptions import AuthenticationError
from swanlab.sdk.cmd import utils
from swanlab.sdk.cmd.guard import with_cmd_lock, without_run
from swanlab.sdk.internal.core_python import client
from swanlab.sdk.internal.pkg import console, fs, helper, nrc, safe, scope
from swanlab.sdk.internal.settings import ROOT_FOLDER, Settings
from swanlab.sdk.internal.settings import settings as global_settings
from swanlab.sdk.typings.cmd import LoginType
from swanlab.sdk.typings.pkg.client.bootstrap import LoginResponse

__all__ = ["login", "login_cli", "login_raw"]


@with_cmd_lock
@without_run("login")
def login(
    api_key: Optional[str] = None,
    relogin: bool = False,
    host: Optional[str] = None,
    save: LoginType = False,
    timeout: int = 10,
) -> bool:
    """Authenticate with SwanLab Cloud.

    This function authenticates your environment with SwanLab. If already logged in
    and `relogin` is False, this function does nothing. Call this before `swanlab.init()`
    to use cloud features.

    :param api_key: Your SwanLab API key. If not provided, will attempt to read from
        environment or prompt for input.

    :param relogin: If True, forces re-authentication and overwrites existing credentials.
        Defaults to False.

    :param host: Custom API host URL. If not provided, uses the default SwanLab cloud host.

    :param save: Whether to save the API key locally for future sessions. Defaults to False.

    :param timeout: Network request timeout in seconds. Defaults to 10.

    :return: True if login was successful, False otherwise.

    :raises RuntimeError: If called while a run is active.

    :raises AuthenticationError: If login fails due to invalid credentials or network issues.

    Examples:

        Login with an API key:

        >>> import swanlab
        >>> swanlab.login(api_key="your_api_key_here")
        >>> swanlab.init(mode="cloud")

        Interactive login (prompts for API key):

        >>> import swanlab
        >>> swanlab.login()
        >>> swanlab.init(mode="cloud")

        Force re-login and save credentials:

        >>> import swanlab
        >>> swanlab.login(api_key="new_api_key", relogin=True, save=True)
        >>> swanlab.init(mode="cloud")
    """
    pass


def login_raw(
    api_key: Optional[str] = None,
    relogin: bool = False,
    host: Optional[str] = None,
    save: LoginType = False,
    timeout: int = 10,
    wellcome_on_success: bool = True,
    animation: bool = True,
) -> bool:
    # 1. 判断是否允许重新登录
    # 如果已经登录且不需要重新登录，则直接返回
    # 仅当运行时 client 已存在时才视为已登录；本地凭证仅表示可复用，不代表本次会话已完成认证
    pass


def create_client(api_key: str, api_host: str, timeout: int = 10):
    pass


def login_cli(
    api_key: Optional[str] = None,
    relogin: bool = False,
    host: Optional[str] = None,
    save: LoginType = True,
    timeout: int = 10,
) -> bool:
    """
    带循环输入容错的交互式登录接口。
    主要为 CLI 环境或需要极高容错的终端调用设计。
    当捕获到 AuthenticationError 时，如果环境允许交互，则会无限循环提示用户重新输入 API Key。
    """
    pass


def prompt_api_key(
    web_host: str,
    interactive: bool,
    tip: str = "Paste an API key from your profile and hit enter, or press 'CTRL + C' to quit",
    again: bool = False,
) -> str:
    """
    让用户在终端安全地输入 API Key
    输入时内容将被隐藏。完整保留了原本的交互文案与 Windows 专属提示

    :param web_host: 当前 Web 主机地址
    :param interactive: 全局配置是否为交互模式
    :param tip: 提示信息
    :param again: 是否为重试模式，重试模式下会略微调整提示信息以区分首次输入与重试输入

    :raises RuntimeError: 如果当前环境不支持交互式输入
    :return: 用户输入的 API Key
    """
    pass


def wellcome(login_resp: Optional[LoginResponse]):
    """
    登录成功后打印欢迎信息
    :param login_resp: 登录响应对象，包含用户信息等数据
    :return:
    """
    pass
