from datetime import date
from exceptions import *

class Lesson:

    def __init__(self, date_value: date, nameAudit: str, namePrepod: str):
        self.date = date_value
        self.nameAudit = nameAudit
        self.namePrepod = namePrepod

    @classmethod
    def initLesson(cls, line):
        line = line.strip()

        date_str = line[:10]
        try:
            date_Y, date_m, date_d = date_str.split("-")
            dateCl = date(int(date_Y), int(date_m), int(date_d))
        except:
            raise InvalidDateError("Неправильная дата")

        line = line[10:].strip()
        if not line.startswith('"'):
            raise FormatError("Неправильно заполнена аудитория") 
        line = line[1:]
        nameAudit = line[:line.find('"')]
        if nameAudit.strip() == "":
            raise EmptyAuditError("Не заполнена аудитория")

        line = line[line.find('"') + 1:].strip()
        if not line.startswith('"'):
            raise FormatError("Неправильно заполнено имя преподавателя")
        line = line[1:]
        namePrepod = line[:line.find('"')]
        if namePrepod.strip() == "":
            raise EmptyPrepodError("Не заполнено имя преподавателя")

        return cls(dateCl, nameAudit, namePrepod)

    def getParams(self):
        return [self.date, self.nameAudit, self.namePrepod]

    def __str__(self):
        return f'{self.date} "{self.nameAudit}" "{self.namePrepod}"\n'