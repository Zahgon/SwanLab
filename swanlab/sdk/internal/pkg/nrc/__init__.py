"""
@author: cunyue
@file: __init__.py
@time: 2026/4/15 21:16
@description: Netrc 工具，提供纯粹的凭证底层文件读写
"""

import netrc
import os
import shutil
import stat
from pathlib import Path
from typing import Optional, Tuple
from urllib.parse import urlsplit

from .. import fs, safe

__all__ = ["fmt", "read", "write"]


def path(p: Path):
    """
    获取 netrc 文件的完整路径
    """
    pass


def fmt(host: str) -> str:
    """
    格式化域名，移除路由等后缀，仅保留协议、端口、域名，如果没有协议，自动添加 https 协议

    :param host: 需要格式化的 host 字符串

    :raises ValueError: 当 host 为空或仅包含空白字符时抛出
    """
    pass


def read(p: Path) -> Optional[Tuple[str, str, str]]:
    """
    读取 netrc 文件中的凭证信息，依次返回 api_key, api_host, web_host

    映射规则（与写入一致）：
        - machine (host) -> api_host
        - login (username) -> web_host
        - password -> api_key

    :param p: netrc 文件路径
    :return: (api_key, api_host, web_host)，读取失败返回 None
    """

    pass


def write(nrc_path: Path, api_host: str, web_host: str, api_key: str):
    """
    将凭证写入 netrc 文件。
    遵循全局单点登录原则：每次写入都会清空其他所有历史/不同环境的登录凭证。
    """
    # 1. 核心防御
    # 检查字段是否合法
    pass


def remove(nrc_path: Path) -> None:
    """
    删除 netrc 文件中的所有凭证条目。
    遵循全局单点登录原则：直接清空整个 hosts 字典并写回文件。
    如果文件不存在则不做任何操作。
    """
    pass
