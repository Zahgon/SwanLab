"""
@author: cunyue
@file: git.py
@time: 2026/3/30
@description: Git 信息采集
"""

import subprocess
from pathlib import PurePosixPath
from typing import Optional

from swanlab.sdk.internal.pkg import safe
from swanlab.sdk.typings.run.system import GitSnapshot


def get() -> GitSnapshot:
    """创建 GitSnapshot 对象"""
    pass


@safe.decorator(level="debug", message="Failed to get git remote url")
def get_remote_url() -> str:
    """获取 Git 远程仓库地址"""
    pass


@safe.decorator(level="debug", message="Failed to get git branch")
def get_branch() -> str:
    """获取当前分支名"""
    pass


@safe.decorator(level="debug", message="Failed to get git commit")
def get_commit() -> Optional[str]:
    """获取最新提交 hash"""
    pass


def parse_git_url(url: str) -> str:
    """将 SSH 格式转换为 HTTPS 格式"""
    pass
