#!/usr/bin/env python3
from dataclasses import dataclass
from enum import Enum
from rich.console import Console

console = Console()


class Side(Enum):
    LEFT, RIGHT, TOP, BOTTOM = range(4)


sides = {
    "┼": (Side.TOP, Side.BOTTOM, Side.LEFT, Side.RIGHT),
    "│": (Side.TOP, Side.BOTTOM),
    "─": (Side.LEFT, Side.RIGHT),
    "├": (Side.TOP, Side.BOTTOM, Side.RIGHT),
    "┤": (Side.TOP, Side.BOTTOM, Side.LEFT),
    "┬": (Side.BOTTOM, Side.LEFT, Side.RIGHT),
    "┴": (Side.TOP, Side.LEFT, Side.RIGHT),
}


@dataclass
class Wire:
    repr: str
    color: str

    grid: list = None
    powered = False

    @property
    def sides(self) -> tuple[Side]:
        return sides[self.repr]

    def is_connected(self, neighbor: "Wire", side: Side):
        ...

    @property
    def neighbors(self) -> list["Wire"]:
        ...

    def evaluate_power(self):
        ...

    def print(self):
        console.print(self.repr, style=self.color, end="")


def main():
    ...


if __name__ == "__main__":
    main()
