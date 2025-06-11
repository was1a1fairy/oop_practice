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

    def sound(self, sound):
        print(sound)

cat = Animal('Милана', "кошка", 7)
print(cat)
print(cat.sound(input("input sound >> ")))

class Book:

    def __init__(
            self,
            title:str,
            author: str,
            count_pages: int,
    ):
        self.title = title
        self.author = author
        self.count_pages = count_pages

    def __str__(self):
        return (f"Название книги: {self.title}\n,"
                f" Автор: {self.author}\n,"
                f" Количество страниц: {self.count_pages}.")

    def open(
            self,
            page: int
    ):
        if page<=self.count_pages and page>0:
           return f"book open on page {page}"
        else:
            return "incorrect page"

book = Book("Книга:)", "someone", 666)
print(book)
print(book.open(input("input page number >> ")))
