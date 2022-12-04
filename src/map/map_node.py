class Node:
    x: int
    y: int
    value: int
    left_neighbor = None
    right_neighbor = None
    top_neighbor = None
    bottom_neighbor = None

    def __repr__(self) -> str:
        return f"x: {self.x}, y: {self.y}, value: {self.value}"

    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}, value: {self.value}"