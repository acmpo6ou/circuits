from core.wire import Wire, Side, sides


class Lamp(Wire):
    sides = sides["┼"]

    def __init__(self):
        super().__init__("💡", "")

    @property
    def neighbors(self) -> list["Wire"]:
        x, y = self.position()
        neighbors = []

        for side in Side:
            dx, dy = side.value
            try:
                neighbor = self.grid[y + dy][x + dx]
                if not self.is_connected(neighbor, side):
                    continue
            except IndexError:
                continue
            neighbors.append(neighbor)
        return neighbors

    def evaluate_power(self):
        red = any(neighbor.powered for neighbor in self.neighbors if neighbor.color == "red")
        blue = any(neighbor.powered for neighbor in self.neighbors if neighbor.color == "blue")
        self.powered = red and blue
