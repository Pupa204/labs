from lesson import Lesson
from fileWorker import FileWorker

class CommandWorker:

    def __init__(self, items):
        self.items = items

    def execute_file(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                self.execute_command(line.strip())

    def execute_command(self, line):

        if line.startswith("ADD"):
            data = line[4:]
            obj = Lesson.initLesson(data)
            self.items.append(obj)

        elif line.startswith("REM"):
            condition = line[4:].strip()

            field, value = condition.split("==")
            field = field.strip()
            value = value.strip().strip('"')

            if field == "audit":
                self.items = [x for x in self.items if x.nameAudit != value]

            elif field == "prepod":
                self.items = [x for x in self.items if x.namePrepod != value]

            elif field == "date":
                self.items = [x for x in self.items if str(x.date) != value]

        elif line.startswith("SAVE"):
            filename = line.split()[1]

            worker = FileWorker()
            worker.file_name = filename
            worker.data_save(self.items)

        