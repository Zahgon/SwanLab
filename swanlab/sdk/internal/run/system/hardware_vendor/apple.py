"""
@author: cunyue
@file: apple.py
@time: 2026/3/31 01:51
@description: 苹果统一芯片（Apple Silicon）相关的硬件供应商信息和功能实现
对于原本的Intel架构的Mac，我们在cpu.py和memory.py中统一采集信息
"""

import json
import multiprocessing
import subprocess
import sys
from typing import Optional, Tuple

import psutil

from swanlab.sdk.internal.pkg import safe
from swanlab.sdk.typings.run.system import AppleSiliconSnapshot, SystemScalar, SystemScalars, SystemShim
from swanlab.sdk.typings.run.system.hardware_vendor import AppleSiliconProtocol
from swanlab.utils import generate_color


class Apple(AppleSiliconProtocol):
    """
    苹果统一芯片（Apple Silicon）相关的硬件供应商信息和功能实现
    在macOS-arm平台上替代CPU和Memory模块，统一采集CPU、内存相关指标
    """

    @classmethod
    def new(cls, shim: SystemShim) -> Optional[Tuple["Apple", SystemScalars]]:
        # 只有macOS-arm架构才支持苹果统一芯片
        pass

    @staticmethod
    @safe.decorator(level="debug", message="Failed to get Apple Silicon info")
    def get() -> Optional[AppleSiliconSnapshot]:
        pass
