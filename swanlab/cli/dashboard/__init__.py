"""
@author: caddiesnew
@file: __init__.py
@time: 2026/4/1 16:09
@description: CLI Dashboard 模块：watch 命令，依赖于 swanboard
"""

import os
import socket
import sys

import click


def _get_free_port(address: str = "0.0.0.0", default_port: int = 5092) -> int:
    """获取一个可用端口。默认返回 5092，如果被占用，返回一个随机可用端口。"""
    pass


@click.command()
@click.argument(
    "path",
    type=click.Path(
        exists=True,
        dir_okay=True,
        file_okay=False,
        resolve_path=True,
        readable=True,
    ),
    nargs=1,
    required=False,
    default=None,
)
@click.option(
    "--host",
    "-h",
    default="127.0.0.1",
    type=str,
    nargs=1,
    help="The host of swanlab web, default by 127.0.0.1",
)
@click.option(
    "--port",
    "-p",
    default=None,
    nargs=1,
    type=click.IntRange(1, 65535),
    help="The port of swanlab web, default by 5092",
)
@click.option(
    "--logdir",
    "-l",
    default=None,
    nargs=1,
    type=click.Path(
        exists=True,
        dir_okay=True,
        file_okay=False,
        resolve_path=True,
        readable=True,
    ),
    help="Specify the folder to store Swanlog. Deprecated: use `swanlab watch <LOG PATH>` instead.",
)
@click.option(
    "--log-level",
    default="info",
    nargs=1,
    type=click.Choice(["debug", "info", "warning", "error", "critical"]),
    help="The level of log, default by info.",
)
def watch(path: str, host: str, port: int, logdir: str, log_level: str):
    """Run this command to turn on the SwanLab dashboard service."""
    pass
