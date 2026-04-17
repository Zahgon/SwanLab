"""
@author: cunyue
@file: consumer.py
@time: 2026/3/13
@description: SwanLab 后台消费者线程
"""

import queue
import threading
from abc import ABC
from typing import Set

from swanlab.proto.swanlab.metric.column.v1.column_pb2 import ColumnType
from swanlab.sdk.internal.bus.emitter import RunQueue
from swanlab.sdk.internal.bus.events import (
    CondaEvent,
    ConfigEvent,
    ConsoleEvent,
    FlushPayload,
    MetadataEvent,
    MetricLogEvent,
    RequirementsEvent,
    ScalarDefineEvent,
)
from swanlab.sdk.internal.context import RunContext
from swanlab.sdk.internal.pkg import console, safe

from .record_builder import RecordBuilder


class ConsumerProtocol(ABC):
    """消费者协议"""

    def __init__(
        self,
        ctx: RunContext,
        event_queue: RunQueue,
        builder: RecordBuilder,
        flush_timeout: float = 0.5,
        batch_size: int = 100,
    ): ...

    def start(self) -> None: ...

    def stop(self) -> None: ...

    def join(self) -> None: ...


class StopEvent:
    pass


_STOP = StopEvent()


class BackgroundConsumer(ConsumerProtocol):
    def __init__(
        self,
        ctx: RunContext,
        event_queue: RunQueue,
        builder: RecordBuilder,
        flush_timeout: float = 0.5,
        batch_size: int = 100,
    ):
        pass

    def start(self) -> None:
        pass

    def join(self) -> None:
        pass

    def stop(self) -> None:
        pass

    def _run(self) -> None:
        pass

    def _flush(self, records: FlushPayload) -> None:
        """处理一批 Record：持久化、回调、上传等"""
        pass
