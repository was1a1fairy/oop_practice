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
        return ((self.end.y - self.start.y)+(self.end.x - self.start.x))**0.5

class Money:

    def __init__(
            self,
            dollars: int,
            cents: int
    ):
        self.dollars = dollars + cents//100
        self.cents = cents//100

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
        self.seconds = seconds%(60*60)
        self.minutes = minutes%60 + seconds%60
        self.hours = hours + minutes//60 + seconds//3600

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

    def __len__(self):
        return self.hours*60*60 + self.minutes*60 + self.seconds

class ColoredPoint(Point):

    def __init__(self, x:int, y:int, color:str):
        super().__init__(x,y)
        self.color = color

    def __str__(self):
        return (f"point({self.x},{self.y})"
                f" have {self.color} color")

    def __add__(self, other: ColoredPoint):
        if self.color == other.color:
            return ColoredPoint(self.x + other.x,
                                self.y + other.y,
                                self.color)
        else:
            return ColoredPoint(self.x + other.x,
                                self.y + other.y,
                                "black")

    def __sub__(self, other: ColoredPoint):
        if self.color == other.color:
            return ColoredPoint(self.x - other.x,
                                self.y - other.y,
                                self.color)
        else:
            return ColoredPoint(self.x - other.x,
                                self.y - other.y,
                                "black")

class Matrix:

    def __init__(
            self,
            a:int,
            b:int,
            c:int,
            d:int
    ):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self):
        return f"{[[self.a,self.b],
                   [self.c,self.d]]}"

    def __add__(self, other: Matrix):
        return Matrix(self.a + other.a,
                      self.b + other.b,
                      self.c + other.c,
                      self.d + other.d)

    def __mul__(self, value: int):
        return Matrix(self.a * value,
                      self.b * value,
                      self.c * value,
                      self.d * value)

    def __len__(self):
        return 4

class Temperature:

    def __init__(self, degrees: int):
        self.degrees = degrees

    def __str__(self):
        return f"temperature: {self.degrees}"

    def __add__(self, other: Temperature):
        return Temperature(self.degrees + other.degrees)

    def __sub__(self, other: Temperature):
        return Temperature(self.degrees - other.degrees)

    def __mul__(self, value: int):
        return Temperature(self.degrees*value)