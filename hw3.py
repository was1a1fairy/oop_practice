from __future__ import annotations

class BankAccount:

    def __init__(
            self,
            owner: str,
            balance:str
    ):
        self.__owner = owner
        self.__balance = balance

    def get_owner(self):
        return self.__owner

    def get_balance(self):
        return self.__balance

    def set_owner(self, owner: str):
        if type(owner) != str:
            raise ValueError("ewwww, please? input str")
        self.__owner = owner

    def set_balance(self, balance: (int or float)):
        if not isinstance(balance, (int or float)) and balance>0:
            raise ValueError("...input valid value, please!!")
        self.__balance = balance

class Rectangle:

    def __init__(
            self,
            width:int or float,
            height: int or float
    ):
        self.__width = width
        self.__height = height

    def get_width(self) -> float:
        return self.__width

    def get_height(self) -> float:
        return self.__height

    def set_width(self, width: int or float):
        if not (isinstance(width, (int, float)) and width>0):
            raise ValueError("ну ты совсем, норм число вводи")
        self.__width = width

    def set_height(self, height: int or float):
        if not isinstance(height, (int, float)) and height>0:
            raise ValueError("научитесь вводить числа")
        self.__height = height

    def area(self) -> float:
        return self.__height * self.__width

class Student:

    def __init__(
            self,
            name: str,
            grades: list
    ):
        self.__name = name
        self.__grades = grades

    def get_name(self):
        return self.__name

    def get_grades(self):
        return self.__grades

    def set_name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("input str!!!!!")
        self.__name = name

    def set_grades(self, grades: list):
        if not isinstance(grades, list):
            raise TypeError("научитесь вводить списки")
        for i in range(len(grades)):
            if not isinstance(grades[i], int):
                raise TypeError("научитесь вводить целые числа")
        self.__grades = grades

    def average(self):
        return sum(self.__grades)/len(self.__grades)

class TemperatureLog:

    def __init__(
            self,
            city: str,
            temperatures: list
    ):
        self.__city = city
        self.__temperatures = temperatures

    def get_city(self):
        return self.__city

    def get_temperatures(self):
        return self.__temperatures

    def set_city(self, city: str):
        if not isinstance(city, str):
            raise TypeError("научитесь вводить строки")
        self.__city = city

    def set_temperatures(self, temps: list):
        if not isinstance(temps, list):
            raise TypeError("научитесь вводить списки")
        for i in range(len(temps)):
            if not(len(temps)==7 and type(temps[i])==(int or float)):
                raise ValueError("научитесь вводить числа")
        self.__temperatures = temps

    def average_temp(self):
        return sum(self.__temperatures)/len(self.__temperatures)

    def max_temp(self):
        return max(self.__temperatures)

    def min_temp(self):
        return min(self.__temperatures)


class EmployeePayroll:

    def __init__(
            self,
            name: str,
            salary: int or float,
            tax_rate: int or float
    ):
        self.__name = name
        self.__salary = salary
        self.__tax_rate = tax_rate

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def get_tax_rate(self):
        return self.__tax_rate

    def set_name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("введите правильно хотя бы имя")
        self.__name = name

    def set_salary(self, sal: float):
        if not isinstance(sal, (int or float)):
            raise TypeError("введите число")
        if sal<0:
            raise ValueError("число должно быть дольше нуля")
        self.__salary = sal

    def set_tax_rate(self, rate: float):
        if rate>=1 or rate<=0:
            raise ValueError("введите рейтинг от 0 до 1")
        self.__tax_rate = rate

    def net_salary(self):
       return (self.__salary * (1 - self.__tax_rate))

    def annual_net(self):
        return 12 * EmployeePayroll.net_salary(self)