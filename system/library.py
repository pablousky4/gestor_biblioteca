from database.db_manager import DBManager

class Library:
    def __init__(self):
        self.db = DBManager()
        self.books = self.db.get_all_books()
        self.users = self.db.get_all_users()
        self.employees = self.db.get_all_employees()  

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

    def add_book(self, book):
        self.books.append(book)
        self.db.add_book(book)

    def add_user(self, user):
        self.users.append(user)
        self.db.add_user(user)

    def add_employee(self, name, position):
        self.db_manager.add_employee(name, position)
        self.employees = self.db_manager.get_all_employees() 