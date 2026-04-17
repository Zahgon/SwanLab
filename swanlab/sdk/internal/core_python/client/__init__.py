"""
@author: cunyue
@file: __init__.py
@time: 2026/3/7 14:04
@description: SwanLab 运行时客户端，用于与 SwanLab API 进行交互
"""

from typing import Optional, Union

from swanlab.sdk.internal.pkg import client, console

__all__ = ["exists", "reset", "new", "get", "post", "put", "patch", "delete"]

# ==============================================================================
# 模块级全局状态与代理快捷函数
# ==============================================================================

_default_client: Optional[client.Client] = None


def new(api_key: str, base_url: str, timeout: int = 10) -> client.Client:
    """创建一个新的 SwanLab 运行时客户端。"""
    pass


def exists() -> bool:
    """检查当前的 SwanLab 运行时客户端是否已存在。"""
    pass


def reset():
    """重置/销毁当前的 SwanLab 运行时客户端。"""
    pass


def _get_client() -> client.Client:
    """获取当前的默认客户端。"""
    pass


def get(url: str, params: Optional[dict] = None, retries: Optional[int] = None):
    pass


def post(url: str, data: Optional[Union[dict, list]] = None, retries: Optional[int] = None):
    pass


def put(url: str, data: Optional[dict] = None, retries: Optional[int] = None):
    pass


def patch(url: str, data: Optional[dict] = None, retries: Optional[int] = None):
    pass


def delete(url: str, retries: Optional[int] = None):
    pass
