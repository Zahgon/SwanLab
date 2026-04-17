"""
@author: cunyue
@file: __init__.py
@time: 2026/3/7 14:18
@description: SwanLab SDK 辅助函数
"""

from .env import DEBUG, is_interactive, is_jupyter
from .version import get_swanlab_latest_version, get_swanlab_version

__all__ = [
    "DEBUG",
    "is_jupyter",
    "is_interactive",
    "strip_none",
    "get_swanlab_version",
    "get_swanlab_latest_version",
]


def strip_none(data: dict, strip_empty_dict: bool = True, strip_empty_str: bool = False) -> dict:
    """
    递归剔除字典中的 None 值。

    :param data: 待处理的字典
    :param strip_empty_dict: 是否连同空字典一起剔除（包含剔除 None 后变为空的嵌套字典），默认为 True
    :param strip_empty_str: 是否连同空字符串一起剔除，仅当 strip_empty_dict 为 True 时有效，默认为 False
    """
    pass
