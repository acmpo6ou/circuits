#!/usr/bin/env python3
from dataclasses import dataclass
from enum import Enum
from rich.console import Console

console = Console()


class Side(Enum):
    TOP = (0, -1)
    BOTTOM = (0, 1)
    RIGHT = (1, 0)
    LEFT = (-1, 0)


sides = {
    "┼": (Side.TOP, Side.BOTTOM, Side.LEFT, Side.RIGHT),
    "│": (Side.TOP, Side.BOTTOM),
    "─": (Side.LEFT, Side.RIGHT),
    "├": (Side.TOP, Side.BOTTOM, Side.RIGHT),
    "┤": (Side.TOP, Side.BOTTOM, Side.LEFT),
    "┬": (Side.BOTTOM, Side.LEFT, Side.RIGHT),
    "┴": (Side.TOP, Side.LEFT, Side.RIGHT),
}

inverse = {
    Side.TOP: Side.BOTTOM,
    Side.BOTTOM: Side.TOP,
    Side.LEFT: Side.RIGHT,
    Side.RIGHT: Side.LEFT,
}


@dataclass
class Wire:
    repr: str
    color: str

    grid: list[list["Wire"]] = None
    powered = False

    def position(self):
        for x, row in enumerate(self.grid):
            try:
                y = row.index(self)
            except ValueError:
                continue
            return x, y

    @property
    def sides(self) -> tuple[Side]:
        return sides[self.repr]

    def is_connected(self, neighbor: "Wire", side: Side):
        return side in self.sides and inverse[side] in neighbor.sides

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
