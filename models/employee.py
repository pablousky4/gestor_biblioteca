class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def add_book(self, library, book):
        library.books.append(book)

    def add_user(self, library, user):
        library.users.append(user)
