"""
@author: cunyue
@file: helper.py
@time: 2026/3/7 17:49
@description: SwanLab 运行时客户端辅助函数
"""

import json
from typing import Dict, List, Optional, Tuple, Union

import requests

from swanlab.sdk.internal.pkg import safe


def decode_response(resp: requests.Response) -> Union[Dict, List, str]:
    """
    解码响应，合并异常捕获
    """
    pass


@safe.decorator(message=None)
def decode_error_response(resp: requests.Response) -> Optional[Tuple[str, str]]:
    """
    尝试从错误响应的 JSON body 中解码业务错误码 (code) 和错误信息 (message)。
    如果响应为空、非 JSON 格式或缺少字段，装饰器会捕获异常并返回 None。

    :param resp: 错误响应
    :return: (code, message) 元组。如果解析失败则返回 None
    """
    # 如果响应体为空，提前结束
    pass
