"""
@author: cunyue
@file: memory.py
@time: 2026/3/31 01:50
@description: 内存信息模块
"""

import subprocess
import sys
from typing import Optional, Tuple

import psutil

from swanlab.sdk.internal.pkg import safe
from swanlab.sdk.typings.run.system import MemorySnapshot, SystemScalar, SystemScalars, SystemShim
from swanlab.sdk.typings.run.system.hardware_vendor import MemoryProtocol
from swanlab.utils import generate_color


def _bytes_to_snapshot(total_bytes: int, MB: int = 1024**2, GB: int = 1024**3) -> Optional[MemorySnapshot]:
    """将字节数转换为合适单位的 MemorySnapshot，优先 GB，不足 1 GB 时用 MB"""
    pass


class Memory(MemoryProtocol):
    """
    内存信息模块
    这是通用的内存信息采集实现，全部使用Python标准库，设计上这属于兜底的内存采集实现
    """

    @classmethod
    def new(cls, shim: SystemShim) -> Optional[Tuple["Memory", SystemScalars]]:
        pass

    @staticmethod
    @safe.decorator(level="debug", message="Failed to get memory info")
    def get() -> Optional[MemorySnapshot]:
        pass

    @staticmethod
    @safe.decorator(level="debug", message="Failed to get total memory bytes")
    def _get_total_bytes(timeout_seconds=2.0) -> Optional[int]:
        """获取系统总内存字节数"""
        pass
