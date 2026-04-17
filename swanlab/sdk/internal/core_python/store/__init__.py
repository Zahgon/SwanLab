"""
@author: cunyue
@file: __init__.py
@time: 2025/6/5 16:32
@description: 记录的数据遵循LevelDB格式：https://github.com/google/leveldb/blob/main/doc/log_format.md
我们使用 crc32 计算数据校验和，crc32 相对轻量，且计算速度较快
DataStore 大致代码借鉴自 W&B

文件头版本区分了不同更新时的格式变化，这方面我们不会做向下兼容，即低版本文件不一定能被新版本读取，可以通过版本降级来区分不同版本号
"""

import os
import struct
import zlib
from typing import IO, Any, Optional, Tuple

from swanlab.exceptions import DataStoreError

__all__ = ["DataStoreWriter", "DataStoreReader", "DataStoreError"]

LEVELDBLOG_HEADER_LEN = 7
LEVELDBLOG_BLOCK_LEN = 32768
LEVELDBLOG_DATA_LEN = LEVELDBLOG_BLOCK_LEN - LEVELDBLOG_HEADER_LEN

LEVELDBLOG_FULL = 1
LEVELDBLOG_FIRST = 2
LEVELDBLOG_MIDDLE = 3
LEVELDBLOG_LAST = 4

LEVELDBLOG_HEADER_IDENT = b":SWL"
LEVELDBLOG_HEADER_MAGIC = 0xE1D6  # zlib.crc32(bytes("SwanLab", 'utf-8')) & 0xffff
LEVELDBLOG_HEADER_VERSION = 1

# 模块级 CRC 预计算，构造一次，读写两侧共用
_CRC = [0] * (LEVELDBLOG_LAST + 1)
for _x in range(1, LEVELDBLOG_LAST + 1):
    _CRC[_x] = zlib.crc32(bytes([_x])) & 0xFFFFFFFF


# ===========================================================================
# 写入
# ===========================================================================


class DataStoreWriter:
    """追加写入器，持有一个长期打开的二进制文件句柄。"""

    def __init__(self):
        pass

    def open(self, filename: str) -> None:
        """创建并初始化文件，文件已存在时抛出 FileExistsError。"""
        pass

    def write(self, data: bytes) -> None:
        """写入任意字节，遵循 LevelDB log 分块规范。"""
        pass

    def ensure_flushed(self) -> None:
        pass

    def close(self) -> None:
        pass

    def _write_record(self, data: bytes, data_type: int = LEVELDBLOG_FULL) -> None:
        pass


# ===========================================================================
# 读取
# ===========================================================================


class DataStoreReader:
    """顺序扫描读取器，实现迭代器协议。"""

    def __init__(self):
        pass

    def open(self, filename: str) -> None:
        """打开文件并校验文件头。"""
        pass

    def scan(self) -> Optional[bytes]:
        """读取下一条完整记录，到达文件末尾时返回 None。"""
        pass

    def close(self) -> None:
        pass

    def __iter__(self):
        pass

    def __next__(self) -> bytes:
        pass

    def _read_header(self) -> None:
        pass

    def _read_record(self) -> Optional[Tuple[int, bytes]]:
        pass
