"""
@author: cunyue
@file: __init__.py
@time: 2026/3/13 21:37
@description: SwanLab SDK CMD 守卫函数，用于检查运行时状态和实现线程安全
"""

import os
import threading
from functools import wraps
from typing import Callable

from swanlab.sdk.internal.run import has_run

_CMD_LOCK = threading.Lock()
_CMD_PID = os.getpid()


def with_cmd_lock(func):
    """
    全局锁装饰器。
    注意：此锁为不可重入锁 (Lock)，如果两个被此装饰器装饰的 API 相互调用，必定发生死锁
    fork 后子进程中此锁可能处于已持有状态，检测到 fork 时替换为新锁
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        pass

    return wrapper


def with_run(cmd: str):
    """
    装饰器：要求必须有 run 在运行，否则抛出 RuntimeError

    :param cmd: 命令名称
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            pass

        return wrapper

    return decorator


def without_run(cmd: str):
    """
    装饰器：要求必须没有 run 在运行，否则抛出 RuntimeError
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            pass

        return wrapper

    return decorator
