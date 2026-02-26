from interface import InterfaceApp
from lesson import Lesson
from fileWorker import FileWorker
import tkinter as tk

root = tk.Tk()
repository = FileWorker()
app = InterfaceApp(root, repository)
root.mainloop()