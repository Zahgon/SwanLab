"""
@author: cunyue
@file: record_builder.py
@time: 2026/3/13
@description: protobuf Record 工厂，覆盖所有 record_type
"""

from functools import singledispatchmethod
from typing import List, Type

from google.protobuf.timestamp_pb2 import Timestamp

from swanlab.proto.swanlab.config.v1.config_pb2 import ConfigRecord
from swanlab.proto.swanlab.metric.column.v1.column_pb2 import ColumnClass, ColumnRecord, ColumnType, SectionType
from swanlab.proto.swanlab.record.v1.record_pb2 import Record
from swanlab.proto.swanlab.system.v1.console_pb2 import ConsoleRecord
from swanlab.proto.swanlab.system.v1.env_pb2 import CondaRecord, MetadataRecord, RequirementsRecord
from swanlab.sdk.internal.bus.events import (
    CondaEvent,
    ConfigEvent,
    ConsoleEvent,
    MetadataEvent,
    ParseResult,
    RequirementsEvent,
    ScalarDefineEvent,
)
from swanlab.sdk.internal.context import RunContext, TransformMedia
from swanlab.sdk.internal.context.transformer import TransformData
from swanlab.sdk.internal.pkg import adapter, fs
from swanlab.sdk.internal.run.transforms import Scalar


class RecordBuilder:
    def __init__(self, ctx: RunContext):
        pass

    def _wrap(self, **kwargs) -> Record:
        """统一附加 num(自增) + timestamp，返回 Record envelope"""
        pass

    # ── 用户数据 ──

    @singledispatchmethod
    def build_log(self, value, key: str, timestamp: Timestamp, step: int) -> ParseResult:
        """默认回退：标量"""
        pass

    @build_log.register(list)
    def _(self, value: List[TransformMedia], key: str, timestamp: Timestamp, step: int) -> ParseResult:
        """媒体对象数组
        dispatch 并不能识别每个数组元素的类型，因此还需手动检查
        """
        pass

    @build_log.register(TransformMedia)
    def _(self, value: TransformMedia, key: str, timestamp: Timestamp, step: int) -> ParseResult:
        """将单个 TransformMediaType 转换为 DataRecord"""
        pass

    def build_column_from_log(self, cls: Type[TransformData], key: str) -> Record:
        """隐式创建列：从 TransformType 推断 ColumnType，并同步 RunMetrics"""
        pass

    def build_column_from_scalar_define(self, event: ScalarDefineEvent) -> Record:
        """显式创建标量列（DefineEvent）"""
        pass

    # ── 系统元数据 ──

    def build_config(self, event: ConfigEvent) -> Record:
        """构建 ConfigRecord envelope"""
        pass

    def build_console(self, event: ConsoleEvent) -> Record:
        """构建 ConsoleRecord envelope"""
        pass

    def build_metadata(self, event: MetadataEvent) -> Record:
        """构建 MetadataRecord envelope"""
        pass

    def build_requirements(self, event: RequirementsEvent) -> Record:
        """构建 RequirementsRecord envelope"""
        pass

    def build_conda(self, event: CondaEvent) -> Record:
        """构建 CondaRecord envelope"""
        pass
