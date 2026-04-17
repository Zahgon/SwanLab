"""
@author: cunyue
@file: _parse.py
@time: 2026/3/14
@description: Config 值序列化——纯函数，无副作用，无外部依赖
"""

import argparse
import datetime
import json
import math
from collections.abc import MutableMapping
from dataclasses import asdict, is_dataclass
from typing import Any, cast

__all__ = ["parse", "json_serializable", "adapt_third_party"]

# 基础原生类型（子类需要向上转型）
_BASE_TYPES = (int, float, str)


def json_serializable(obj: Any) -> Any:
    """
    将任意 Python 对象递归转换为 JSON 可序列化的基础类型。

    特殊值处理：
    - float NaN  → 字符串 "NaN"
    - float Inf  → 字符串 "Inf"
    - bool 优先于 int 处理（bool 继承自 int）
    - 子类类型（如 numpy.int64）→ 强制转回父类原生类型

    :raises TypeError: 对象无法被序列化
    """
    pass


def adapt_third_party(data: Any) -> dict:
    """
    适配第三方配置对象，转换为普通 dict。

    支持：
    - omegaconf.DictConfig
    - mmengine.Config
    - argparse.Namespace
    - dataclass 实例

    :raises TypeError: 未能命中任何适配器
    """
    # omegaconf
    pass


def parse(config: Any) -> dict:
    """
    将 config 转换为 JSON 可序列化的 dict。

    转换策略（按优先级依次尝试）：
    1. 第三方类型适配（omegaconf、mmengine、argparse、dataclass）
    2. json_serializable 递归转换
    3. json.dumps / json.loads 兜底

    :raises TypeError: 所有策略均失败
    """
    pass
