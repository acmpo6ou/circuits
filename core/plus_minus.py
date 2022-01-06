from core.wire import Wire, sides


class PlusMinus(Wire):
    sides = sides["┼"]
    powered = True

    def __init__(self, repr_: str):
        super().__init__(repr_, "red" if repr_ == "+" else "blue")

    def evaluate_power(self):
        pass
