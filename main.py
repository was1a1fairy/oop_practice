# 1

class Animal:

    def __init__(
            self,
            name: str,
            type:str,
            age: int
    ):
        self.name = name
        self.type = type
        self.age = age

    def __str__(self):
        return (f"Имя животного: {self.name},"
                f" Вид животного: {self.type},"
                f" Возраст животного: {self.age}")

