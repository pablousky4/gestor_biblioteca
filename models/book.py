from models.genre import BookGenre

class Book:
    def __init__(self, title, author, genre: BookGenre, available=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available

    def is_available(self):
        return self.available

    def borrow(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        self.available = True
