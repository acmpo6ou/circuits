#!/usr/bin/env python3
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


def main():
    ...


if __name__ == "__main__":
    main()
