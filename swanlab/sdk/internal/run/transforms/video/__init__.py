"""
@author: cunyue
@file: __init__.py
@time: 2026/3/15
@description: 视频处理模块，暂时只支持 GIF
"""

import hashlib
from io import BytesIO
from pathlib import Path
from typing import List, Optional

from google.protobuf.timestamp_pb2 import Timestamp

from swanlab.proto.swanlab.metric.column.v1.column_pb2 import ColumnType
from swanlab.proto.swanlab.metric.data.v1.data_pb2 import DataRecord
from swanlab.proto.swanlab.metric.data.v1.media.video_pb2 import VideoItem, VideoValue
from swanlab.sdk.internal.context import TransformMedia
from swanlab.sdk.internal.pkg import fs
from swanlab.sdk.typings.run.transforms import CaptionType
from swanlab.sdk.typings.run.transforms.video import VideoDataType

# 各格式的魔数校验表，新增格式时在此追加
# format → (magic_bytes, ...)
_FORMAT_MAGIC: dict[str, tuple[bytes, ...]] = {
    "gif": (b"GIF87a", b"GIF89a"),
}

# 路径后缀 → 格式名
_EXT_TO_FORMAT: dict[str, str] = {
    ".gif": "gif",
}


def _detect_format_by_magic(data: bytes) -> Optional[str]:
    """根据魔数推断格式，无法识别则返回 None"""
    pass


class Video(TransformMedia):
    def __init__(self, data_or_path: VideoDataType, caption: CaptionType = None):
        """Video class constructor

        目前支持的格式：GIF。

        Parameters
        ----------
        data_or_path: str, bytes, BytesIO, or Video
            Path to a supported video file, raw video bytes, a BytesIO containing
            video data, or another Video instance (nesting).
        caption: str, optional
            Caption for the video.
        """
        pass

    @classmethod
    def column_type(cls) -> ColumnType:
        pass

    @classmethod
    def build_data_record(cls, *, key: str, step: int, timestamp: Timestamp, data: List[VideoItem]) -> DataRecord:
        pass

    def transform(self, *, step: int, path: Path) -> VideoItem:
        pass
