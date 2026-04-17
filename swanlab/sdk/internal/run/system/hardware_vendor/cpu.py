"""
@author: cunyue
@file: cpu.py
@time: 2026/3/31 01:50
@description: CPU 信息模块
"""

import multiprocessing
import platform
import subprocess
import sys
from typing import Optional, Tuple

import psutil

from swanlab.sdk.internal.pkg import safe
from swanlab.sdk.typings.run.system import CPUSnapshot, SystemScalar, SystemScalars, SystemShim
from swanlab.sdk.typings.run.system.hardware_vendor import CpuProtocol
from swanlab.utils import generate_color


class CPU(CpuProtocol):
    """
    CPU 信息模块
    这是通用的 CPU 信息采集实现，全部使用python标准库，设计上这属于兜底的CPU采集实现
    """

    @classmethod
    def new(cls, shim: SystemShim) -> Optional[Tuple["CPU", SystemScalars]]:
        pass

    @staticmethod
    @safe.decorator(level="debug", message="Failed to get CPU info")
    def get() -> Optional[CPUSnapshot]:
        # 1. 获取 CPU 品牌
        pass

    @staticmethod
    @safe.decorator(level="debug", message="Failed to get real CPU brand")
    def _get_real_brand() -> Optional[str]:
        """尝试获取真实的 CPU 品牌名称"""
        pass
