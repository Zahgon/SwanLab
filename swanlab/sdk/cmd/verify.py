"""
@author: caddiesnew
@file: verify.py
@time: 2026/4/9 21:00
@description: verify 方法，验证当前登录状态
"""

from rich.text import Text

from swanlab.sdk.cmd import utils
from swanlab.sdk.internal.pkg import console, nrc
from swanlab.sdk.internal.pkg.client.bootstrap import login_by_api_key
from swanlab.sdk.internal.settings import settings
from swanlab.sdk.typings.cmd import LoginType

__all__ = ["verify_cli"]


def verify_cli(save: LoginType = "root") -> bool:
    # 1. 检查本地是否存在 API Key
    pass
