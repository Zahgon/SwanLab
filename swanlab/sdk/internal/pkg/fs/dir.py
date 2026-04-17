"""
@author: cunyue
@file: dir.py
@time: 2026/3/11 13:44
@description: SwanLab SDK 目录辅助函数
"""

import os
import tempfile
import time
from pathlib import Path
from typing import Union

from .. import console


def _get_fs_timeout(default: float = 5.0) -> float:
    """
    安全地从环境变量获取文件系统超时时间
    防范用户输入非数字 ("abc") 或非法数字 (-1.0) 导致模块导入崩溃
    """
    pass


# 模块加载时安全获取
TIMEOUT = _get_fs_timeout()


def safe_mkdirs(*paths: Union[str, Path], timeout: float = TIMEOUT):
    """
    安全地创建多个目录。
    :param paths: 目录路径列表
    :param timeout: 超时时间（秒）
    """
    pass


def safe_mkdir(path: Union[str, Path], timeout: float = TIMEOUT) -> Path:
    """
    安全地创建目录，带有抗 NAS 异步延迟的探针机制。
    :param path: 目录路径
    :param timeout: 超时时间（秒）
    """
    pass
