class Point:
    def __init__(self, x:int, y:int) -> None:
        self.X = x
        self.Y = y

    def __repr__(self) -> str:
        return f"({self.X},{self.Y})"
        