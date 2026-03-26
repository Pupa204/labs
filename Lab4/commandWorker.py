from lesson import Lesson

class CommandWorker:
    def __init__(self, items, error_callback=None):
        self.items = items
        self.show_error = error_callback

    def execute_file(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    self.execute_command(line)
        except Exception as e:
            if self.show_error:
                self.show_error(f"Ошибка при открытии файла команд: {e}")
            else:
                print(f"Ошибка при открытии файла команд: {e}")

    def execute_command(self, line):
        try:
            # ADD
            if line.startswith("ADD"):
                data = line[4:]
                obj = Lesson.initLesson(data)
                self.items.append(obj)

            # REM
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

            # SAVE
            elif line.startswith("SAVE"):
                filename = line.split()[1]
                with open(filename, "w", encoding="utf-8") as f:
                    for item in self.items:
                        f.write(str(item))

        except Exception as e:
            if self.show_error:
                self.show_error(f"Ошибка при выполнении команды '{line}': {e}")
            else:
                print(f"Ошибка при выполнении команды '{line}': {e}")