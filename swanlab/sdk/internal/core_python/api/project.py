"""
@author: cunyue
@file: project.py
@time: 2026/3/10 18:00
@description: SwanLab 运行时项目API
"""

from typing import Optional, cast

from swanlab.exceptions import ApiError
from swanlab.sdk.internal.core_python import client
from swanlab.sdk.internal.pkg import helper
from swanlab.sdk.internal.pkg.client.utils import decode_response
from swanlab.sdk.typings.core_python.api.project import InitProjectType, ProjectType


def get_project(*, username: str, name: str) -> ProjectType:
    """
    获取项目信息
    :param username: 项目所属的用户名
    :param name: 项目名称
    :return: 项目信息
    """
    pass


def get_or_create_project(*, username: Optional[str], name: str, public: bool) -> InitProjectType:
    """
    创建项目，如果项目已存在，则获取项目信息
    :param name: 项目名称
    :param username: 项目所属的用户名
    :param public: 项目是否公开
    :return: 项目信息
    """
    pass
