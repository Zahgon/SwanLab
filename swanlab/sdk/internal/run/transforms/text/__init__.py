"""
@author: cunyue
@file: __init__.py
@time: 2026/3/11 19:17
@description: 文本处理模块
"""

import hashlib
from pathlib import Path
from typing import List

from google.protobuf.timestamp_pb2 import Timestamp

from swanlab.proto.swanlab.metric.column.v1.column_pb2 import ColumnType
from swanlab.proto.swanlab.metric.data.v1.data_pb2 import DataRecord
from swanlab.proto.swanlab.metric.data.v1.media.text_pb2 import TextItem, TextValue
from swanlab.sdk.internal.context import TransformMedia
from swanlab.sdk.internal.pkg import fs
from swanlab.sdk.typings.run.transforms import CaptionType
from swanlab.sdk.typings.run.transforms.text import TextDataType


class Text(TransformMedia):
    def __init__(self, content: TextDataType, caption: CaptionType = None):
        pass

    @classmethod
    def column_type(cls) -> ColumnType:
        pass

    @classmethod
    def build_data_record(cls, *, key: str, step: int, timestamp: Timestamp, data: List[TextItem]) -> DataRecord:
        pass

    def transform(self, *, step: int, path: Path) -> TextItem:
        # 计算 sha256
        pass
