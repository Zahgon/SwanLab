"""
@author: cunyue
@file: __init__.py
@time: 2026/3/15
@description: 图像处理模块
"""

import hashlib
from io import BytesIO
from pathlib import Path
from typing import List, Optional, get_args

from google.protobuf.timestamp_pb2 import Timestamp

from swanlab import vendor
from swanlab.proto.swanlab.metric.column.v1.column_pb2 import ColumnType
from swanlab.proto.swanlab.metric.data.v1.data_pb2 import DataRecord
from swanlab.proto.swanlab.metric.data.v1.media.image_pb2 import ImageItem, ImageValue
from swanlab.sdk.internal.context import TransformMedia
from swanlab.sdk.internal.pkg import fs
from swanlab.sdk.typings.run.transforms import CaptionType
from swanlab.sdk.typings.run.transforms.image import ImageDataType, ImageFileType, ImageModeType, ImageSizeType

ACCEPT_FORMAT = ["png", "jpg", "jpeg", "bmp"]


def _is_torch_tensor(obj) -> bool:
    """通过类型名检测 PyTorch Tensor，避免强制导入 torch"""
    pass


def _resize(image: "vendor.PIL.Image.Image", size) -> "vendor.PIL.Image.Image":
    """按 size 参数缩放图像"""
    pass


class Image(TransformMedia):
    def __init__(
        self,
        data_or_path: ImageDataType,
        mode: ImageModeType = None,
        caption: CaptionType = None,
        file_type: ImageFileType = None,
        size: ImageSizeType = None,
    ):
        """Image class constructor

        Parameters
        ----------
        data_or_path: str, PIL.Image.Image, numpy.ndarray, torch.Tensor, matplotlib.figure.Figure, or Image
            Path to an image file (PNG/JPG/JPEG/BMP; GIF is not supported), a PIL Image,
            numpy array (shape: (H, W) or (H, W, 3/4)), torch.Tensor, matplotlib figure,
            or another Image instance (nesting).
        mode: str, optional
            PIL mode applied when converting to PIL.Image (e.g. 'RGB', 'L').
        caption: str, optional
            Caption for the image.
        file_type: str, optional
            Output file format. One of ['png', 'jpg', 'jpeg', 'bmp']. Defaults to 'png'.
        size: int, list, or tuple, optional
            Resize policy:
            - int: maximum side length (aspect-ratio preserved via thumbnail).
            - (w, h): exact target size.
            - (w, None) / (None, h): fix one dimension, scale the other proportionally.
            - None: no resize.
        """
        pass

    @classmethod
    def column_type(cls) -> ColumnType:
        pass

    @classmethod
    def build_data_record(cls, *, key: str, step: int, timestamp: Timestamp, data: List[ImageItem]) -> DataRecord:
        pass

    def transform(self, *, step: int, path: Path) -> ImageItem:
        pass
