import tkinter as tk
from tkinter import messagebox, simpledialog

from models.book import Book
from models.genre import BookGenre
from models.user import User
from system.library import Library


class LibraryGUI:
    def __init__(self, root):
        self.library = Library()
        self.root = root
        self.root.title("Sistema de Gestión de Biblioteca")

        # Interfaz
        tk.Button(root, text="Agregar Libro", command=self.add_book).pack(pady=5)
        tk.Button(root, text="Agregar Usuario", command=self.add_user).pack(pady=5)
        tk.Button(root, text="Prestar Libro", command=self.borrow_book).pack(pady=5)
        tk.Button(root, text="Devolver Libro", command=self.return_book).pack(pady=5)
        tk.Button(root, text="Consultar Disponibilidad", command=self.check_availability).pack(pady=5)
        tk.Button(root, text="Salir", command=self.save_and_exit).pack(pady=10)

    def add_book(self):
        title = simpledialog.askstring("Título del libro", "Ingrese el título:")
        author = simpledialog.askstring("Autor del libro", "Ingrese el autor:")
        genre_str = simpledialog.askstring("Género (FICTION, NONFICTION, SCIENCE, ART)", "Ingrese el género:")
        try:
            genre = BookGenre[genre_str.upper()]
        except KeyError:
            messagebox.showerror("Error", "Género inválido.")
            return

        book = Book(title, author, genre)
        self.library.books.append(book)
        messagebox.showinfo("Éxito", f"Libro '{title}' agregado.")

    def add_user(self):
        name = simpledialog.askstring("Nombre del usuario", "Ingrese el nombre:")
        if self.library.find_user(name):
            messagebox.showinfo("Info", "El usuario ya existe.")
        else:
            user = User(name)
            self.library.users.append(user)
            messagebox.showinfo("Éxito", f"Usuario '{name}' agregado.")

    def borrow_book(self):
        username = simpledialog.askstring("Nombre del usuario", "Ingrese su nombre:")
        title = simpledialog.askstring("Título del libro", "Ingrese el título:")
        user = self.library.find_user(username)
        book = self.library.find_book(title)

        if user and book:
            if user.borrow_book(book):
                messagebox.showinfo("Éxito", f"{username} ha prestado '{title}'.")
            else:
                messagebox.showwarning("No disponible", f"'{title}' no está disponible.")
        else:
            messagebox.showerror("Error", "Usuario o libro no encontrado.")

    def return_book(self):
        username = simpledialog.askstring("Nombre del usuario", "Ingrese su nombre:")
        title = simpledialog.askstring("Título del libro", "Ingrese el título:")
        user = self.library.find_user(username)
        book = self.library.find_book(title)

        if user and book:
            if user.return_book(book):
                messagebox.showinfo("Éxito", f"'{title}' ha sido devuelto por {username}.")
            else:
                messagebox.showwarning("Error", "Este usuario no tiene prestado ese libro.")
        else:
            messagebox.showerror("Error", "Usuario o libro no encontrado.")

    def check_availability(self):
        title = simpledialog.askstring("Consultar libro", "Ingrese el título:")
        book = self.library.find_book(title)
        if book:
            estado = "Disponible" if book.is_available() else "Prestado"
            messagebox.showinfo("Estado", f"'{title}' está {estado}.")
        else:
            messagebox.showerror("Error", "Libro no encontrado.")

    def save_and_exit(self):
        # Simulación de guardado
        self.root.quit()
