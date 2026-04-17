"""
@author: cunyue
@file: session.py
@time: 2026/3/7 17:50
@description: SwanLab 运行时客户端会话辅助函数
具有默认重试次数和超时时间，也支持自定义重试次数和超时时间
"""

import contextvars
import copy
import time
from typing import Optional

from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from swanlab.exceptions import ApiError
from swanlab.sdk.internal.pkg import console, helper

from .utils import decode_error_response

__all__ = ["create", "TimeoutHTTPAdapter", "SessionWithRetry", "request_retries_ctx"]
VERSION_HEADER = "X-SwanLab-SDK-Version"
TRACE_ID = "swanlab.client"
# 用于存储当前请求的重试次数，避免在请求中传递 retries 参数
request_retries_ctx: contextvars.ContextVar[Optional[int]] = contextvars.ContextVar("request_retries", default=None)


class TimeoutHTTPAdapter(HTTPAdapter):
    """
    支持默认超时的 HTTPAdapter。
    """

    def __init__(self, *args, **kwargs):
        self.timeout = kwargs.pop("timeout", None)
        super().__init__(*args, **kwargs)

    def send(self, request, *args, **kwargs):
        pass


class SessionWithRetry(Session):
    """
    支持在请求级别自定义重试次数的 Session。
    通过拦截 retries 参数并将其转化为隐式 Header 传递给 Adapter。
    """

    def request(self, method, url, *args, **kwargs):
        retries = kwargs.pop("retries", None)

        if retries is not None:
            # 3. 将自定义参数放入上下文，并获取 token 以便后续清理
            token = request_retries_ctx.set(retries)
            try:
                return super().request(method, url, *args, **kwargs)
            finally:
                # 4. 请求结束后，务必清理上下文，避免影响复用该线程的其他请求
                request_retries_ctx.reset(token)
        else:
            return super().request(method, url, *args, **kwargs)

    def send(self, request, **kwargs):
        """
        重写底层发送方法，统一处理所有响应的校验逻辑和网络日志记录
        """
        pass

    # ---------------------------------- 类型提示占位符，保留以保证 IDE 友好 ----------------------------------

    def get(self, url, params=None, retries: Optional[int] = None, **kwargs):
        return self.request("GET", url, params=params, retries=retries, **kwargs)

    def options(self, url, retries: Optional[int] = None, **kwargs):
        pass

    def head(self, url, retries: Optional[int] = None, **kwargs):
        pass

    def post(self, url, data=None, json=None, retries: Optional[int] = None, **kwargs):
        return self.request("POST", url, data=data, json=json, retries=retries, **kwargs)

    def put(self, url, data=None, retries: Optional[int] = None, **kwargs):
        return self.request("PUT", url, data=data, retries=retries, **kwargs)

    def patch(self, url, data=None, retries: Optional[int] = None, **kwargs):
        return self.request("PATCH", url, data=data, retries=retries, **kwargs)

    def delete(self, url, retries: Optional[int] = None, **kwargs):
        pass


def create(timeout: int = 60, default_retry: int = 5) -> SessionWithRetry:
    """
    创建一个挂载了超时和重试机制的会话实例。
    """
    session = SessionWithRetry()

    retry_strategy = Retry(
        total=default_retry,
        backoff_factor=0.5,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=frozenset(["GET", "POST", "PUT", "DELETE", "PATCH"]),
        raise_on_status=False,
    )

    adapter = TimeoutHTTPAdapter(max_retries=retry_strategy, timeout=timeout)

    session.mount("https://", adapter)
    session.mount("http://", adapter)
    session.headers[VERSION_HEADER] = helper.get_swanlab_version()
    return session
