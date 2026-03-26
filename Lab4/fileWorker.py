from lesson import Lesson
from exceptions import LessonError


class FileWorker:
    file_name = "data.txt"

    def data_read(self):
        items = []
        with open(self.file_name, "r", encoding='utf-8') as f:
            for line in f:
                try:
                    obj = Lesson.initLesson(line)

                    if obj:
                        items.append(obj)

                except LessonError as e:
                    print(f"Ошибка: {e} в строке - {line.strip()}")

        return items

    def data_save(self, items):
        with open(self.file_name, 'w', encoding='utf-8') as f:
            for item in items:
                f.write(str(item))