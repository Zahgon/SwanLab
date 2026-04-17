"""
@author: cunyue
@file: __init__.py
@time: 2026/4/14 00:38
@description: SwanLab 客户端对象，与服务器进行交互
"""

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Optional, Union

import requests

from swanlab.exceptions import AuthenticationError
from swanlab.sdk.typings.pkg.client.bootstrap import LoginResponse

from .. import console, helper, nrc, scope
from . import session
from .bootstrap import login_by_api_key
from .utils import decode_response

__all__ = ["Client", "session", "ApiResponse", "decode_response"]


@dataclass
class ApiResponse:
    data: Any
    raw: requests.Response


class Client:
    """
    封装 SwanLab HTTP 请求的核心客户端对象。
    仅负责请求、重试拦截及鉴权生命周期管理。
    """

    # 提前刷新的缓冲时间（7天）
    REFRESH_TIME = 60 * 60 * 24 * 7

    def __init__(self, api_key: str, base_url: str, timeout: int = 10):
        pass

    def _refresh_auth(self, timeout: int = 10, warning: bool = True) -> Optional[LoginResponse]:
        """
        刷新鉴权信息。
        直接更新当前会话的 Cookie，保留底层连接池以提升性能。
        """
        pass

    def _before_request(self):
        """请求前置检查。距过期时间不足安全缓冲期时，触发刷新。"""
        pass

    # ---------------------------------- 实例 HTTP 方法 ----------------------------------
    def request(self, method: str, url: str, **kwargs):
        """基础请求方法封装"""
        pass

    def get(self, url: str, params: Optional[dict] = None, retries: Optional[int] = None):
        pass

    def post(self, url: str, data: Optional[Union[dict, list]] = None, retries: Optional[int] = None):
        pass

    def put(self, url: str, data: Optional[dict] = None, retries: Optional[int] = None):
        pass

    def patch(self, url: str, data: Optional[dict] = None, retries: Optional[int] = None):
        pass

    def delete(self, url: str, retries: Optional[int] = None):
        pass
