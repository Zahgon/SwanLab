"""
@author: caddiesnew
@file: thread.py
@time: 2026/4/16
@description: 事件驱动的 Record 上传守护线程
"""

import threading
from typing import Callable, List, Optional

from swanlab.proto.swanlab.record.v1.record_pb2 import Record
from swanlab.sdk.internal.pkg import console
from swanlab.sdk.internal.pkg.safe import block as safe_block

from .buffer import RecordBuffer
from .dispatch import Dispatch
from .sender import HttpRecordSender


class Transport:
    """
    事件驱动的 Record Action 线程。

    用 Condition 驱动上传事件：
    - put() 时 notify() 立刻唤醒线程，延迟接近 0
    - wait(timeout=batch_interval) 保证最大攒批间隔
    - 清空 buffer 后在锁外委托 Dispatch，不阻塞生产者
    """

    BATCH_INTERVAL: float = 1.0
    FINISH_JOIN_TIMEOUT: int = 30
    THREAD_NAME: str = "SwanLab·Transport"

    def __init__(
        self,
        batch_interval: Optional[float] = None,
        upload_callback: Optional[Callable[[int], None]] = None,
        sender: Optional[HttpRecordSender] = None,
        auto_start: bool = True,
    ):
        pass

    def start(self) -> None:
        """启动守护线程。"""
        pass

    def put(self, records: List[Record]) -> None:
        """追加 records 到 buffer 并唤醒线程。"""
        pass

    def finish(self) -> None:
        """
        通知线程停止，等待最终排空，由线程自行关闭 sender。

        设计要点：
        - _loop 的 finally 块负责 _close_sender()，保证线程退出前 sender 可用。
        - finish() 仅设置 _finished flag 并 join，不在 join 后关闭 sender，
          避免线程仍在 dispatch 时 sender 被 use-after-close。
        - join timeout 设为 30s 以覆盖弱网下多 chunk 重试场景；
          超时后线程仍为 daemon 线程会随进程退出，不会泄漏。
        """
        pass

    def _close_sender(self) -> None:
        pass

    # ── 线程主循环 ──

    def _loop(self) -> None:
        pass


__all__ = [
    "Transport",
]
