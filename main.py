import tkinter as tk
from ui.gui import LibraryGUI

def main():
    root = tk.Tk()
    app = LibraryGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
