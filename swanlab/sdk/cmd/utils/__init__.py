"""
@author: cunyue
@file: __init__.py
@time: 2026/4/16 01:18
@description: cmd 模块工具函数
"""

from functools import wraps
from pathlib import Path

from swanlab.sdk.internal.pkg import console, fs, nrc
from swanlab.sdk.internal.settings import ROOT_FOLDER, settings
from swanlab.sdk.typings.cmd import LoginType

__all__ = ["get_nrc_path"]


def get_nrc_path(save: LoginType) -> Path:
    """根据登录类型获取 NRC 文件路径"""
    pass


def append_gitignore(path: Path):
    """在指定路径下创建 .gitignore 文件"""
    pass


def with_loading_animation(message: str = "Initializing SwanLab...", spinner_name: str = "dots"):
    """
    一个使用 rich 包装的加载动画装饰器
    :param message: 动画旁边显示的文字
    :param spinner_name: 动画样式（如 'dots', 'bouncingBar', 'point' 等）
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 使用 rich 的 status 作为上下文管理器包裹函数的执行
            pass

        return wrapper

    return decorator
