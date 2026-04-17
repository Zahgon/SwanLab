"""
@author: cunyue
@file: env.py
@time: 2026/3/8 17:57
@description: SwanLab SDK 环境相关工具
"""

import io
import os
import sys

__all__ = ["is_jupyter", "is_interactive", "DEBUG"]

# 设计上，DEBUG 变量独立于其他模块，包括 settings。但是我们又希望有一个环境变量去控制是否打印 debug 信息，所以这里额外绑定一个环境变量
DEBUG = os.getenv("SWANLAB_DEBUG", "false").lower() in ["true", "1", "yes", "on"]
"""
是否为调试模式
"""


def is_jupyter() -> bool:
    """判断当前是否在 Jupyter Notebook 环境中"""
    pass


def is_interactive() -> bool:
    """
    是否为可交互式环境（输入连接tty设备）
    特殊的环境：jupyter notebook
    """
    pass
