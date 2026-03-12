from tkinter import ttk, messagebox
from datetime import datetime
from lesson import Lesson
from fileWorker import FileWorker
from exceptions import LessonError

class InterfaceApp:
    def __init__(self, root, repo):
        self.root = root
        self.repo = repo
        self.items = self.repo.data_read()

        self.setup_ui()
        self.refresh_table()

    def setup_ui(self):
        main_frame = ttk.Frame(self.root)
        main_frame.pack(padx=10, pady=10, fill="both", expand=True)

        input_frame = ttk.LabelFrame(main_frame, text="Управление записями")
        input_frame.pack(fill="x", pady=(0, 10))

        ttk.Label(input_frame, text="Дата:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.ent_date = ttk.Entry(input_frame, width=12)
        self.ent_date.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.ent_date.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Аудитория:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.ent_nameAudit = ttk.Entry(input_frame, width=15)
        self.ent_nameAudit.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(input_frame, text="Имя преподавателя:").grid(row=0, column=4, padx=5, pady=5, sticky="w")
        self.ent_namePrepod = ttk.Entry(input_frame, width=20)
        self.ent_namePrepod.grid(row=0, column=5, padx=5, pady=5)

        button_frame = ttk.Frame(input_frame)
        button_frame.grid(row=1, column=0, columnspan=8, pady=10)

        btn_add = ttk.Button(button_frame, text="Добавить запись", command=self.add_item, width=20)
        btn_add.pack(side="left", padx=5)

        btn_del = ttk.Button(button_frame, text="Удалить выбранное", command=self.delete_item, width=20)
        btn_del.pack(side="left", padx=5)

        self.table = ttk.Treeview(self.root, columns=("date", "nameAudit", "namePrepod"), show="headings")
        self.table.heading("date", text="Дата")
        self.table.heading("nameAudit", text="Аудитория")
        self.table.heading("namePrepod", text="Имя")
        self.table.pack(padx=10, pady=5, fill="both")

    def refresh_table(self):
        for row in self.table.get_children():
            self.table.delete(row)
        for item in self.items:
            self.table.insert("", "end", values=item.getParams())

    def add_item(self):
        raw_data = f'{self.ent_date.get()} "{self.ent_nameAudit.get()}" "{self.ent_namePrepod.get()}"'

        try:
            new_obj = Lesson.initLesson(raw_data)
            self.items.append(new_obj)
            self.repo.data_save(self.items)
            self.refresh_table()
        except LessonError as e:
            print(f"Ошибка при добавлении записи: {e}")

    def delete_item(self):
        selected = self.table.selection()
        if not selected:
            return
        for item_id in selected:
            index = self.table.index(item_id)
            del self.items[index]
        self.repo.data_save(self.items)
        self.refresh_table()