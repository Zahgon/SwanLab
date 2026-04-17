"""
@author: cunyue
@file: requirements.py
@time: 2026/3/30
@description: 依赖包信息采集
"""

import subprocess
from typing import Optional

from swanlab.sdk.internal.pkg import safe


def _try_run(cmd: list, timeout: int = 5, check: bool = False) -> Optional[subprocess.CompletedProcess]:
    """尝试执行命令，命令不存在时返回 None 而不是抛异常"""
    pass


@safe.decorator(level="debug", message="Failed to get environment requirements")
def get() -> str:
    """获取当前环境依赖"""
    # 尝试 pixi
    pass
