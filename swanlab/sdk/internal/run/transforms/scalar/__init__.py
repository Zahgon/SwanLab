"""
@author: cunyue
@file: __init__.py
@time: 2026/3/11 16:32
@description: 标量处理模块
"""

import math
from typing import Any, Union

from google.protobuf.timestamp_pb2 import Timestamp

from swanlab.proto.swanlab.metric.column.v1.column_pb2 import ColumnType
from swanlab.proto.swanlab.metric.data.v1.data_pb2 import DataRecord
from swanlab.proto.swanlab.metric.data.v1.scalar.scalar_pb2 import ScalarValue
from swanlab.sdk.internal.context import TransformData
from swanlab.sdk.internal.pkg import safe


class Scalar(TransformData):
    def __init__(self):
        pass

    @classmethod
    def column_type(cls) -> ColumnType:
        pass

    @classmethod
    def build_data_record(cls, *, key: str, step: int, timestamp: Timestamp, data: ScalarValue) -> DataRecord:
        pass

    @staticmethod
    def transform(data: Any) -> ScalarValue:
        """
        Scalar 的Transformer比较特殊，不直接转换为Scalar对象而是static方法，这能省去不必要的内存开销。

        此方法用于处理标量数据，包括数字、字符串、布尔值等。

        1. 布尔值：转为 1.0 或 0.0
        2. 数字（int/float）：正常转换为 float
        3. 字符串：尝试转换为数字，如果能转换为数字则转换为数字，否则报错，额外处理 NaN 和 Inf 的情况，此时都返回 NaN

        :param data: 待处理的数据

        :raises TypeError: 如果数据类型不支持转换为浮点数
        """
        # 0. 鸭子类型检测：如果是 Tensor 或 numpy array，尝试提取其标量值
        pass


@safe.decorator(message=None)
def _transform_tensor_or_array(data: Any) -> Union[float, int, str, bool]:
    pass
