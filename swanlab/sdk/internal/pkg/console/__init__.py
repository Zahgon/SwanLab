"""
@author: cunyue
@file: __init__.py
@time: 2026/3/6 13:20
@description: SwanLab SDK 控制台日志模块，负责打印日志
当 SWANLAB_DEBUG=true 时，终端输出会同步镜像到诊断日志文件（通过 log 模块）
"""

import inspect
import os
import sys
from datetime import datetime
from typing import Any, Literal, Optional

from rich.console import Console
from rich.text import Text

from .. import helper
from . import log

__all__ = ["debug", "info", "warning", "error", "trace", "c"]

c = Console()
_name = "swanlab"
_this_file = os.path.abspath(__file__)


def _now() -> str:
    """返回毫秒级时间戳，格式：2026-03-14 10:23:45.124"""
    pass


def _caller_location() -> str:
    """
    遍历调用栈，返回第一个不属于本模块的帧的 module:func:line。
    用于 loguru 风格的调用方定位。
    """
    pass


def _to_plain_text(*args: Any) -> str:
    """
    将 console 的 *args 转为纯文本字符串，用于写入诊断日志文件。
    去除 rich markup，保留原始语义。
    """
    pass


def _loguru_build(
    level_name: str,
    style: str,
    *args,
    location: Optional[str] = None,
    console_args=None,
    file_args=None,
) -> tuple["Text", str]:
    """
    构建 loguru 风格的 Rich Text（终端用）和纯文本字符串（日志文件用），
    两者共享同一份时间戳和调用方位置，确保一致性。
    location 未传时自动从调用栈推导。

    - args: 默认同时用于终端和文件
    - console_args: 若传入，则仅用于终端消息体
    - file_args: 若传入，则仅用于文件消息体
    """
    pass


def _loguru_print(level_name: str, style: str, *args, **kwargs) -> str:
    """
    构建并打印 loguru 风格日志行，同时返回对应的纯文本字符串供写入日志文件。
    2026-03-14 10:23:45.124 | DEBUG  | module:func:line - message
    """
    pass


# -----------------------------------------------------------------------------
# 导出的模块级日志函数
# -----------------------------------------------------------------------------


# noinspection PyShadowingBuiltins
def print(*args, **kwargs):  # noqa: A001
    """发送普通消息"""
    pass


def debug(*args, write_to_file: bool = True, **kwargs):
    """发送调试消息（仅 SWANLAB_DEBUG=true 时输出）
    格式：2026-03-14 10:23:45.124 | DEBUG    | module:func:line - message
    """
    pass


def info(*args, color: str = "blue", **kwargs):
    """发送常规通知
    格式：swanlab: message
    :param color: 前缀 'swanlab' 的颜色，默认蓝色
    """
    pass


def warning(*args, **kwargs):
    """发生警告
    格式：2026-03-14 10:23:45.124 | WARNING  | module:func:line - message
    """
    pass


def error(*args, write_to_file: bool = True, **kwargs):
    """发生错误
    格式：2026-03-14 10:23:45.124 | ERROR    | module:func:line - message
    """
    pass


def trace(
    *args,
    max_frames: int = 2,
    write_to_file: bool = True,
    level_name: Literal["error", "debug"] = "error",
    **kwargs,
):
    """
    打印当前异常栈，是 error/debug 的变体：在消息末尾追加异常栈信息。
    必须在 except 块内调用，否则无操作。

    - 终端：显示最后 max_frames 层栈帧 + 异常类型 + 异常信息
    - 日志文件：显示完整错误栈

    Args:
        *args: 前缀消息
        max_frames: 终端显示的最大栈帧数，默认 2
        write_to_file: 是否写入日志文件，默认 True
        level_name: 日志级别，"error" 或 "debug"，默认 "error"
    """
    pass
