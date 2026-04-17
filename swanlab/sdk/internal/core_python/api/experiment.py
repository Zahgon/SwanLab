"""
@author: cunyue
@file: experiment.py
@time: 2026/3/10 19:02
@description: SwanLab 运行时实验API
"""

from typing import List, Optional

from swanlab.exceptions import ApiError
from swanlab.sdk.internal.core_python import client
from swanlab.sdk.internal.pkg import helper
from swanlab.sdk.typings.run import ResumeType


def create_or_resume_experiment(
    username: str,
    project: str,
    *,
    name: str,
    resume: ResumeType,
    run_id: Optional[str] = None,
    color: str,
    description: Optional[str],
    job_type: Optional[str],
    group: Optional[str],
    tags: Optional[List[str]],
    created_at: Optional[str] = None,
) -> bool:
    """
    初始化实验，获取存储信息
    :param username: 所属用户名
    :param project: 所属项目名称
    :param name: 所属实验名称
    :param resume: 恢复上一次实验的状态
    :param run_id: 上一次实验的ID
    :param color: 实验颜色
    :param description: 实验描述
    :param job_type: 任务类型
    :param group: 实验组
    :param tags: 实验标签
    :param created_at: 实验创建时间，格式为 ISO 8601
    """
    pass
