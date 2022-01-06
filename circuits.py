#!/usr/bin/env python3
from copy import deepcopy

from core.lamp import Lamp
from core.plus_minus import PlusMinus
from core.wire import Wire

# fmt: off
grid = [
    [PlusMinus("+"), PlusMinus("-"), Wire("─", "blue"), Wire("─", "blue"), Wire("┤", "blue")],
    [Wire("├", "red"), Wire("┼", "red"), Wire("┼", "blue"), Wire("┼", "blue"), Wire("┤", "blue")],
    [Wire("├", "red"), Wire("┼", "red"), Wire("┼", "blue"), Wire("┼", "blue"), Wire("┤", "blue")],
    [Wire("├", "red"), Wire("┼", "red"), Wire("┼", "red"), Wire("┼", "blue"), Wire("┤", "blue")],
    [Wire("├", "red"), Wire("─", "red"), Wire("─", "red"), Wire("─", "red"), Lamp()],
]
# fmt: on

for row in grid:
    for wire in row:
        wire.grid = grid

old_state = None


def main():
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
