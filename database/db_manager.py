import sqlite3
from models.genre import BookGenre
from models.book import Book
from models.user import User
from models.employee import Employee

DB_NAME = "library.db"

class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.create_tables()
        self.insert_sample_data()

    def create_tables(self):
        c = self.conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                genre TEXT NOT NULL,
                available INTEGER NOT NULL
            )
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        ''')
        c.execute('''
        CREATE TABLE IF NOT EXISTS employee (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            position TEXT NOT NULL
        )
        ''')
        self.conn.commit()

    def insert_sample_data(self):
        c = self.conn.cursor()

        # Libros de prueba con títulos de dos palabras
        c.execute("SELECT COUNT(*) FROM books")
        if c.fetchone()[0] == 0:
            print("Insertando libros de prueba...")
            books = [
                ("El quijote", "Cervantes", "FICTION", 1),
                ("Silent Spring", "Rachel Carson", "SCIENCE", 1),
                ("Art Theory", "John Smith", "ART", 1),
                ("Hidden Figures", "Margot Lee Shetterly", "NONFICTION", 1)
            ]
            c.executemany('''
                INSERT INTO books (title, author, genre, available)
                VALUES (?, ?, ?, ?)
            ''', books)

        # Usuarios de prueba
        c.execute("SELECT COUNT(*) FROM users")
        if c.fetchone()[0] == 0:
            print("Insertando usuarios de prueba...")
            users = [("Ruben",), ("Alvaro",), ("Nico",)]
            c.executemany('INSERT INTO users (name) VALUES (?)', users)

        # Empleados de prueba
        c.execute("SELECT COUNT(*) FROM employee")
        if c.fetchone()[0] == 0:
            print("Insertando empleados de prueba...")
            employees = [
                ("Carlos García", "Bibliotecario"),
                ("María López", "Asistente"),
                ("Javier Fernández", "Administrador")
            ]
            c.executemany('''
                INSERT INTO employee (name, position)
                VALUES (?, ?)
            ''', employees)

        self.conn.commit()


    def add_book(self, book):
        c = self.conn.cursor()
        c.execute('''
            INSERT INTO books (title, author, genre, available)
            VALUES (?, ?, ?, ?)
        ''', (book.title, book.author, book.genre.name, int(book.available)))
        self.conn.commit()

    def add_user(self, user):
        c = self.conn.cursor()
        c.execute('''
            INSERT OR IGNORE INTO users (name) VALUES (?)
        ''', (user.name,))
        self.conn.commit()

    def get_all_books(self):
        c = self.conn.cursor()
        c.execute('SELECT title, author, genre, available FROM books')
        rows = c.fetchall()
        return [Book(title, author, BookGenre[genre], bool(available)) for title, author, genre, available in rows]

    def get_all_users(self):
        c = self.conn.cursor()
        c.execute('SELECT name FROM users')
        return [User(name,) for (name,) in c.fetchall()]

    def get_all_employees(self):
        c = self.conn.cursor()
        c.execute('SELECT name, position FROM employee')
        return [Employee(name, position) for name, position in c.fetchall()]
    
    def add_employee(self, name, position):
        c = self.conn.cursor()
        c.execute('''
            INSERT INTO employee (name, position)
            VALUES (?, ?)
        ''', (name, position))
        self.conn.commit()