from __future__ import annotations


class Point:

    def __init__(
            self,
            x: int,
            y: int
    ):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x},{self.y}"

    def __add__(self, other: Point):
        return Point(self.x + other.x, self.y + other.y)

     def __sub__(self, other: Point):
         return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, value: int):
        return Point(self.x * value, self.y * value)


class Vector2D:

    def __init__(
            self,
            start: Point,
            end: Point
    ):
        self.start = start
        self.end = end

    def __str__(self):
        return f"Vector: {self.start}, {self.end}"

    def __add__(
            self,
            other: Vector2D
    ):
        return Vector2D(self.start + other.start,
                        self.end + other.end)

    def __sub__(self, other: Vector2D):
        return Vector2D(self.start - other.start,
                        self.end - other.end)

    def __mul__(self, value: int):
        return Vector2D(self.start * value, self.end * value)

    def len(self):
        return (self.end.y - self.start.y)*(self.end.x - self.start.x)
