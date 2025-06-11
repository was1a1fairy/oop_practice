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
        return (f"Название книги: {self.title},\n"
                f" Автор: {self.author},\n"
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
print(book.open(int(input("input page number >> "))))

class PassengerPlane:

    def __init__(
            self,
            manufacturer: str,
            model: str,
            capacity: int,
            current_height: int,
            current_speed: int
    ):
        self.manufacturer = manufacturer
        self.model = model
        self.capacity = capacity
        self.current_height = current_height
        self.current_speed = current_speed

    def __str__(self):
        return (f"Производитель самолёта: {self.manufacturer},\n"
                f" Модель самолёта: {self.model},\n"
                f" Вместимость пассажиров: {self.capacity},\n"
                f" Текущая высота: {self.current_height},\n"
                f" Текущая скорость: {self.current_speed}")

    def takeoff(self, value_for_height: int, value_for_speed: int):
        if self.current_speed==0 or self.current_height==0:
            self.current_height += value_for_height
            self.current_speed += value_for_speed
            print("airplane takeoff!")
        else:
            print("airplane already takeoff:(((")

    def landing(self):
        if self.current_speed==0 or self.current_height==0:
            print("airplane already landed:(((")
        else:
            print("airplane landed!")

    def change_height(self, value: int):
        if value>0 or value<0:
            self.takeoff(value, 0)
            self.current_height += value
            print("height was changed")
        if value==0:
            print('height wasnt changed')

    def change_speed(self, value: int):
        if value>0 or value<0:
            self.takeoff(0, value)
            self.current_speed += value
            print("speed was changed")
        if value==0:
            print('speed wasnt changed')

airplane = PassengerPlane('someone', 'model one', 36, 0, 0)
print(airplane.landing())
print(airplane.takeoff(133, 200))
print(airplane.change_speed(13))
print(airplane.change_height(0))

class MusicAlbum:

    def __init__(
            self,
            player: str,
            title: str,
            style: str,
            playlist: list
    ):
        self.player = player
        self.title = title
        self.style = style
        self.playlist = playlist

    def __str__(self):
        return (f"{self.title}:\n"
                f" {self.playlist}\n"
                f" ({self.player},{self.style})")

    def add_song(self, song: str):
        if song not in self.playlist:
            self.playlist.append(song)
        else:
            print("song already in playlist:(((")

    def del_song(self, song: str):
        if song in self.playlist:
            self.playlist.remove(song)
        else:
            print("Сначала добавьте этот трек в плейлист, а затем удаляйте на здоровье")

    def play_song(self, song: str):
        if song in self.playlist:
            return f"Вопроизведен трек: {song}"

album = MusicAlbum("me", "мяумяу", "rock", [1, 2, 3, 4])
song = "song"
print(album.del_song(song))
print(album.add_song(song))
print(album.play_song(song))