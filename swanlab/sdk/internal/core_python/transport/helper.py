#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
@author: caddiesnew
@file: helper.py
@time: 2026/3/30 15:33
@description: transport 辅助函数
"""

from collections import OrderedDict
from typing import Dict, Iterator, List, Sequence, Tuple

from swanlab.proto.swanlab.record.v1.record_pb2 import Record


def generate_chunks(records: Sequence[Record], max_records_per_request: int) -> Iterator[Tuple[Sequence[Record], int]]:
    """
    按固定大小对 Record 序列做切片。
    yield: (分片数据, 分片长度)
    """
    pass


def group_records_by_type(records: Sequence[Record]) -> Dict[str, List[Record]]:
    """
    使用 WhichOneof("record_type") 按 record 类型分组。

    record_type = record.WhichOneof("record_type") 返回 oneof 中实际设置的字段名，
    如 "start"、"metric" 等，与 proto 定义一一对应。

    返回 OrderedDict 保持插入顺序。
    """
    pass
