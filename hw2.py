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

class Money:

    def __init__(
            self,
            dollars: int,
            cents: int
    ):
        self.dollars = dollars
        self.cents = cents

    def __str__(self):
        return f"{self.dollars} dollars, {self.cents} cents."

    def __add__(self, other: Money):
        return Money((self.dollars + other.dollars) + ((self.cents + other.cents)//100),
        (self.cents + other.cents)%100)

    def __sub__(self, other: Money):
        if self.cents < other.cents:
            self.dollars -= 1
            self.cents += 100
        return Money(self.dollars - other.dollars, self.cents - other.cents)

class Time:

    def __init__(
            self,
            hours,
            minutes,
            seconds
    ):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f"{self.hours} hours, {self.minutes} minutes, {self.seconds} seconds."

    def __add__(self, other: Time):
        minutes = (self.minutes + other.minutes)%60
        seconds = (self.seconds + other.seconds)%60
        hours = self.hours + other.hours
        if self.seconds + other.seconds >= 60:
            minutes += (self.seconds + other.seconds)//60
        if (self.minutes + other.minutes) >= 60:
            hours += (self.minutes + other.minutes)//60
        return Time(hours, minutes, seconds)

    def len(self):
        return self.hours*60*60 + self.minutes*60 + self.seconds