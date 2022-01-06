#!/usr/bin/env python3
import random
from copy import deepcopy

from core.lamp import Lamp
from core.plus_minus import PlusMinus
from core.wire import Wire, sides

old_state = None
grid = []


def gengrid():
    for _ in range(5):
        row = []
        for _ in range(5):
            color = random.choice(("red", "blue"))
            wire = random.choice(list(sides.keys()))
            row.append(Wire(wire, color))
        grid.append(row)

    px, py, mx, my, lx, ly = random.choices(range(5), k=6)
    grid[px][py] = PlusMinus("+")
    grid[mx][my] = PlusMinus("-")
    grid[lx][ly] = Lamp()

    for row in grid:
        for wire in row:
            wire.grid = grid


def main():
    gengrid()
    global old_state

    while True:
        old_state = deepcopy(grid)
        for row in grid:
            for wire in row:
                wire.evaluate_power()

        if old_state == grid:
            break

    for row in grid:
        for wire in row:
            wire.print()
        print()


if __name__ == "__main__":
    main()
