"""
@author: cunyue
@file: __init__.py
@time: 2026/3/11 13:06
@description: SwanLab 数据转换模块，将用户输入的数据封装为Protobuf格式
"""

from typing import Any, List, Type, Union

from swanlab.sdk.internal.context import TransformMedia

from .audio import Audio
from .image import Image
from .scalar import Scalar
from .text import Text
from .video import Video

__all__ = ["Text", "Scalar", "Audio", "Image", "Video", "normalize_media_input"]


def normalize_media_input(
    media_cls: Type[TransformMedia],
    data: Union[Any, List[Any]],
    **kwargs,
) -> List[TransformMedia]:
    """
    规范化媒体输入为统一的列表格式。

    :param media_cls: 媒体类型类（如 Text, Image 等）
    :param data: 单个数据或数据列表（可以是原始数据或已实例化的媒体对象）
    :param kwargs: 额外参数（如 caption），可以是单个值或列表
    :return: 媒体对象列表
    """
    # 如果 data 已经是目标类型的实例列表且无额外参数，直接返回
    pass
