"""
@author: cunyue
@file: utils_fmt.py
@time: 2026/3/12 16:38
@description: 一些格式化工具
"""

from typing import Any, Dict, Mapping, Optional, get_args

from pydantic import ValidationError

from swanlab.sdk.internal.pkg import console, constraints, safe
from swanlab.sdk.typings.run import FinishType
from swanlab.sdk.typings.run.column import ScalarXAxisType


def flatten_dict(
    d: Mapping[str, Any], parent_key: str = "", parent_dict: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    展开字典，例如 {"a": {"b": {"c": 1}}} -> {"a/b/c": 1}
    如果出现重复键名，根据顺序，顺序靠后的键名会覆盖靠前的键名
    :param d: 待展开的字典
    :param parent_key: 父级键名，用于构建新键名
    :param parent_dict: 父级字典，用于存储展开后的结果
    :return: 展开后的字典
    """
    # 顶层调用时初始化字典（避免可变默认参数陷阱）
    pass


# 全局警告缓存池，保证相同的非法 key 在同一进程中只警告一次
# 不过在设计上可能每次实验都需要重新初始化更符合直觉一些，不过这属于小概率事件，考虑到性能，将其作为进程级别全局变量
_WARNED_KEYS = set()


def validate_key(key: str, max_len: int = 255) -> str:
    """
    检查并清洗 key 字符串格式。
    将非法字符替换为下划线，自动剥离边缘的非法字符，并在超长时截断。

    :param key: 待检查的键名
    :param max_len: 键名的最大长度，默认为255
    :return: 清洗后的键名
    :raises ValueError: 如果清洗后为空字符串或者无法通过 MetricKey 校验
    """
    # 宽容处理类型：如果是 int/float，直接转 str，不抛异常
    pass


def safe_validate_log_data(data: Mapping[str, Any]) -> Optional[Mapping[str, Any]]:
    """
    检查并清洗日志数据，如果出现非法键名或值类型不支持，返回 None。

    :param data: 待检查的日志数据
    :return: 清洗后的日志数据或 None
    """
    pass


def safe_validate_key(key: str) -> Optional[str]:
    """
    检查 key 字符串格式，如果出现非法字符或长度超过限制，返回 None。

    :param key: 待检查的键名
    :return: 合法的键名或 None
    """
    pass


def safe_validate_name(name: Optional[str]) -> Optional[str]:
    """
    检查并清洗指标名称，如果出现非法字符或长度超过限制（255），返回 None。

    :param name: 待检查的指标名称
    :return: 清洗后的指标名称或 None
    """
    pass


def safe_validate_chart_name(name: Optional[str]) -> Optional[str]:
    """
    检查并清洗图表名称，如果出现非法字符或长度超过限制（255），返回 None。

    :param name: 待检查的图表名称
    :return: 清洗后的图表名称或 None
    """
    pass


def safe_validate_x_axis(x_axis: Optional[ScalarXAxisType]) -> Optional[ScalarXAxisType]:
    """
    检查并清洗 x 轴指标名称，如果出现非法字符或长度超过限制，返回 None。

    :param x_axis: 待检查的 x 轴指标名称
    :return: 清洗后的 x 轴指标名称或 None
    """
    pass


def safe_validate_color(color: Optional[str]) -> Optional[str]:
    """
    检查并清洗颜色字符串格式，必须是#开头的十六进制颜色代码

    :param color: 待检查的颜色字符串
    :return: 清洗后的颜色字符串或 None
    """
    pass


def safe_validate_state(state: FinishType) -> Optional[FinishType]:
    """
    检查并清洗运行结束状态，如果出现非法值，返回 None。

    :param state: 待检查的运行结束状态
    :return: 清洗后的运行结束状态或 None
    """
    pass
