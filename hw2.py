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

