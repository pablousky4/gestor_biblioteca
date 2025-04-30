class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_user(self, name):
        for user in self.users:
            if user.name.lower() == name.lower():
                return user
        return None
