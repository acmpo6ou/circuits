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

    def position(self) -> tuple[int, int]:
        for y, row in enumerate(self.grid):
            for x, wire in enumerate(row):
                if id(self) == id(wire):
                    return x, y

    @property
    def sides(self) -> tuple[Side]:
        return sides[self.repr]

    def is_connected(self, neighbor: "Wire", side: Side):
        return side in self.sides and inverse[side] in neighbor.sides

    @property
    def neighbors(self) -> list["Wire"]:
        x, y = self.position()
        neighbors = []

        for side in Side:
            dx, dy = side.value
            try:
                neighbor = self.grid[y + dy][x + dx]
                if neighbor.color != self.color or not self.is_connected(neighbor, side):
                    continue
            except IndexError:
                continue
            neighbors.append(neighbor)
        return neighbors

    def evaluate_power(self):
        self.powered = any(neighbor.powered for neighbor in self.neighbors)

    def print(self):
        background = " on white" if self.powered else ""
        console.print(self.repr, style=self.color + background, end="")

    def __eq__(self, other):
        return self.powered == other.powered
