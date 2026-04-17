"""
@author: caddiesnew
@file: logout.py
@time: 2026/4/9 21:00
@description: swanlab.logout 方法，登出 SwanLab 平台
"""

from swanlab.sdk.cmd import utils
from swanlab.sdk.internal.pkg import console, nrc
from swanlab.sdk.internal.settings import settings
from swanlab.sdk.typings.cmd import LoginType

__all__ = ["logout_cli"]


def logout_cli(force: bool = False, save: LoginType = "root") -> bool:
    pass
