"""
@author: cunyue
@file: __init__.py
@time: 2026/3/9 19:09
@description: SwanLab 实验辅助函数，同时作为
"""

import colorsys
import random
import secrets
import string
from typing import Literal, Optional, Union

__all__ = ["generate_color", "generate_id", "generate_name"]


def generate_id(length: int = 8, characters=string.ascii_lowercase + string.digits) -> str:
    """Generate a unique ID for a run or something.

    :param length: The length of the ID. Must be between 1 and 64.
    :param characters: The characters to use for the ID.

    :return: A unique ID string.

    Examples:

        Generate default 8-character ID:

        >>> from swanlab.utils import generate_id
        >>> run_id = generate_id()
        >>> len(run_id)
        8

        Generate custom length ID:

        >>> from swanlab.utils import generate_id
        >>> run_id = generate_id(length=16)
        >>> len(run_id)
        16
    """
    pass


PRESET_COLORS = [
    "#528d59",  # 绿色
    "#587ad2",  # 蓝色
    "#c24d46",  # 红色
    "#9cbe5d",  # 青绿色
    "#6ebad3",  # 天蓝色
    "#dfb142",  # 橙色
    "#6d4ba4",  # 紫色
    "#8cc5b7",  # 淡青绿色
    "#892d58",  # 紫红色
    "#40877c",  # 深青绿色
    "#d0703c",  # 深橙色
    "#d47694",  # 粉红色
    "#e3b292",  # 淡橙色
    "#b15fbb",  # 浅紫红色
    "#905f4a",  # 棕色
    "#989fa3",  # 灰色
]


def generate_color(slug: Optional[Union[Literal["beauty"], int]] = None) -> str:
    """Generate a specific or random color in hexadecimal format.

    :param slug: The slug for the color determination.
        - If None, returns a random color from the preset list.
        - If "beauty", generates a visually appealing random color.
        - If an integer, returns a color from the preset list based on modulo.

    :return: A color in hexadecimal format (e.g., "#FF5733").

    Examples:

        Generate random preset color:

        >>> from swanlab.utils import generate_color
        >>> color = generate_color()
        >>> color.startswith('#')
        True

        Generate beautiful random color:

        >>> from swanlab.utils import generate_color
        >>> color = generate_color("beauty")
        >>> len(color)
        7

        Generate color by index:

        >>> from swanlab.utils import generate_color
        >>> color = generate_color(5)
        >>> color
        '#dfb142'
    """
    # 逻辑 1: 如果传入是 None，随机取一个内部列表中的值
    pass


# 纯粹的动物名词列表
PRESET_ANIMALS = [
    "swan",
    "rat",
    "ox",
    "tiger",
    "rabbit",
    "dragon",
    "snake",
    "horse",
    "goat",
    "monkey",
    "rooster",
    "dog",
    "pig",
    "cat",
    "elephant",
    "penguin",
    "kangaroo",
    "panda",
    "lion",
    "zebra",
]

# "beauty" 模式下的优美形容词
BEAUTY_ADJECTIVES = [
    "elegant",
    "stellar",
    "vibrant",
    "serene",
    "cosmic",
    "lucid",
    "radiant",
    "ethereal",
    "nimble",
    "valiant",
    "gentle",
    "brilliant",
    "luminous",
    "tranquil",
    "dazzling",
]


def generate_name(slug: Optional[Union[Literal["beauty"], int]] = None) -> str:
    """Generate a specific or random entity name.

    :param slug: The slug for the name determination.
        - If None, returns a random animal + 4-char random hash (e.g., "swan-a3f9").
        - If "beauty", generates an appealing adjective-animal-number combo (e.g., "stellar-swan-42").
        - If an integer, returns a name based on modulo + the integer itself (e.g., "dragon-128").

    :return: A generated name string.

    Examples:

        Generate random name:

        >>> from swanlab.utils import generate_name
        >>> name = generate_name()
        >>> '-' in name
        True

        Generate beautiful name:

        >>> from swanlab.utils import generate_name
        >>> name = generate_name("beauty")
        >>> name.count('-')
        2

        Generate name by index:

        >>> from swanlab.utils import generate_name
        >>> name = generate_name(128)
        >>> name
        'goat-128'
    """
    # 逻辑 1: 如果传入是 None，随机动物 + 4位随机字符后缀
    pass
