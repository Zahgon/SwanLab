"""
@author: cunyue
@file: __init__.py.py
@time: 2026/3/11 17:55
@description: SwanLab SDK 内部系统组件，如硬件监控、元数据采集、终端日志收集等
"""

import sys
from typing import Optional

from swanlab.sdk.internal.context import RunContext
from swanlab.sdk.internal.run.system.environment import conda, git, requirements, runtime
from swanlab.sdk.internal.run.system.hardware_vendor.apple import Apple
from swanlab.sdk.internal.run.system.hardware_vendor.cpu import CPU
from swanlab.sdk.internal.run.system.hardware_vendor.memory import Memory
from swanlab.sdk.internal.run.system.monitor import Monitor
from swanlab.sdk.typings.run.system import HardwareSnapshot, MetadataSnapshot, SystemEnvironment, SystemShim

__all__ = ["new", "Monitor"]


def new(ctx: RunContext):
    """
    创建硬件监控模块
    """
    pass
