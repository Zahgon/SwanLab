"""
@author: cunyue
@file: exceptions.py
@time: 2026/3/7 21:36
@description: SwanLab 运行时异常定义
"""

from typing import Union

from requests.exceptions import HTTPError

__all__ = ["ApiError", "AuthenticationError", "DataStoreError"]


class ApiError(HTTPError):
    """
    SwanLab API 请求异常。
    封装了从后端解析出的业务错误码 (code) 和错误信息 (message)。
    """

    def __init__(self, response, *, method: str, trace_id: str, code: Union[int, str], message: str):
        pass


class AuthenticationError(Exception):
    """
    SwanLab 认证失败异常。
    """

    pass


class DataStoreError(Exception):
    """
    DataStore 读写异常。
    """

    pass
