"""
@author: caddiesnew
@file: __init__.py
@time: 2026-03-18 00:03:03
@description: SwanLab SDK 轻量级定时任务模块

设计约束：
1. 使用守护线程执行周期任务，避免因忘记清理导致主进程无法退出
2. cancel() 为协作式停止，只会阻止下一轮调度，不会强杀正在执行的任务
3. 支持固定间隔和动态间隔策略；动态策略接收“已完成执行次数”作为输入
4. start()/run() 可重复调用，但运行中再次调用只会输出 debug 日志，不会启动重复线程
"""

import threading
from typing import Callable, Optional, Union

from swanlab.sdk.internal.pkg import console, safe

__all__ = ["Timer"]

Interval = Union[int, float]
IntervalStrategy = Callable[[int], Union[int, float]]
IntervalValue = Union[Interval, IntervalStrategy]


class Timer:
    """
    轻量级周期任务调度器。

    :param task: 需要周期执行的无参函数
    :param interval: 固定间隔（秒）或动态间隔策略。动态策略入参为当前已完成执行次数。
    :param immediate: 是否在启动后先立即执行一次任务，再进入下一轮等待。
    :param name: 后台线程名称，便于调试定位。
    """

    def __init__(
        self,
        task: Callable[[], None],
        *,
        interval: IntervalValue,
        immediate: bool = False,
        name: str = "SwanLab·Timer",
    ) -> None:
        pass

    def start(self) -> "Timer":
        """
        启动定时器。若当前已在运行，则只告警并返回自身。
        """
        pass

    def run(self) -> "Timer":
        """
        兼容旧接口，等价于 start()。
        """
        pass

    def cancel(self) -> None:
        """
        发出停止信号。
        当前正在执行的任务不会被中断，但后续轮次不会再被调度。
        """
        pass

    def join(self, timeout: Optional[float] = None) -> None:
        """
        等待后台线程退出，通常配合 cancel() 使用以保证任务完整收尾。
        """
        pass

    @property
    def execution_count(self) -> int:
        """
        已完成执行次数。
        """
        pass

    @property
    def is_running(self) -> bool:
        """
        当前后台线程是否仍在运行。
        """
        pass

    def _loop(self) -> None:
        pass

    def _execute_once(self) -> None:
        pass

    def _resolve_interval(self) -> float:
        pass

    @staticmethod
    def _normalize_interval(interval: Union[int, float]) -> float:
        pass
