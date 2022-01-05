#!/usr/bin/env python3
from dataclasses import dataclass
from enum import Enum


class Side(Enum):
    LEFT, RIGHT, TOP, BOTTOM = range(4)


@dataclass
class Wire:
    repr: str
    color: str

    grid: list = None
    powered = False

    def is_connected(self, neighbor: "Wire", side: Side):
        ...

    @property
    def neighbors(self) -> list["Wire"]:
        ...

    def evaluate_power(self):
        ...


def main():
    pass


if __name__ == "__main__":
    main()
