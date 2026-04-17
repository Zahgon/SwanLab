"""
@author: cunyue
@file: conda.py
@time: 2026/3/30
@description: Conda 环境信息采集
"""

import subprocess

from swanlab.sdk.internal.pkg import safe


@safe.decorator(level="debug", message="Failed to get conda environment")
def get() -> str:
    """获取 conda 环境信息"""
    pass
