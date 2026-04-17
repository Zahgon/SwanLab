"""
@author: cunyue
@file: __init__.py
@time: 2026/3/11 19:17
@description: 音频处理模块
"""

import hashlib
from io import BytesIO
from pathlib import Path
from typing import List, Optional

from google.protobuf.timestamp_pb2 import Timestamp

from swanlab import vendor
from swanlab.proto.swanlab.metric.column.v1.column_pb2 import ColumnType
from swanlab.proto.swanlab.metric.data.v1.data_pb2 import DataRecord
from swanlab.proto.swanlab.metric.data.v1.media.audio_pb2 import AudioItem, AudioValue
from swanlab.sdk.internal.context import TransformMedia
from swanlab.sdk.internal.pkg import fs
from swanlab.sdk.typings.run.transforms import CaptionType
from swanlab.sdk.typings.run.transforms.audio import AudioDataType, AudioRateType


class Audio(TransformMedia):
    def __init__(self, data_or_path: AudioDataType, sample_rate: AudioRateType = 44100, caption: CaptionType = None):
        """Audio class constructor

        Parameters
        ----------
        data_or_path: str, numpy.ndarray, or Audio
            Path to an audio file, numpy array of audio data (shape: (num_channels, num_frames)),
            or another Audio instance.
        sample_rate: int
            Sample rate of the audio data. Required when input is a numpy array.
        caption: str, optional
            Caption for the audio.
        """
        pass

    @classmethod
    def column_type(cls) -> ColumnType:
        pass

    @classmethod
    def build_data_record(cls, *, key: str, step: int, timestamp: Timestamp, data: List[AudioItem]) -> DataRecord:
        pass

    def transform(self, *, step: int, path: Path) -> AudioItem:
        pass
