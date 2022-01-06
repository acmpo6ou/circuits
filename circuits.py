#!/usr/bin/env python3
from copy import deepcopy

from wire import Wire

# fmt: off
grid = [
    [Wire("┼", "red"), Wire("┼", "blue"), Wire("─", "blue"), Wire("─", "blue"), Wire("┤", "blue")],
    [Wire("├", "red"), Wire("┼", "red"), Wire("┼", "blue"), Wire("┼", "blue"), Wire("┤", "blue")],
    [Wire("├", "red"), Wire("┼", "red"), Wire("┼", "blue"), Wire("┼", "blue"), Wire("┤", "blue")],
    [Wire("├", "red"), Wire("┼", "red"), Wire("┼", "red"), Wire("┼", "blue"), Wire("┤", "blue")],
    [Wire("├", "red"), Wire("─", "red"), Wire("─", "red"), Wire("─", "red"), Wire("┤", "blue")],
]
# fmt: on

for row in grid:
    for wire in row:
        wire.grid = grid

grid[0][0].powered = True
grid[0][1].powered = True

old_state = None


def main():
    global old_state

    while True:
        old_state = deepcopy(grid)
        for row in grid:
            for wire in row:
                if wire.position() in ((0, 0), (1, 0)):
                    continue
                wire.evaluate_power()

        if old_state == grid:
            break

    for row in grid:
        for wire in row:
            wire.print()
        print()


if __name__ == "__main__":
    main()
