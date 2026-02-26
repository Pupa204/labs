from datetime import date

class Lesson():
    def __init__(self, date: date, nameAudit: str, namePrepod: str):
        self.date = date
        self.nameAudit = nameAudit
        self.namePrepod = namePrepod
    
    @classmethod
    def initLesson(self, line):
        line = line.strip()
        date_Y, date_m, date_d = line[:10].split("-")
        dateCl = date(int(date_Y), int(date_m), int(date_d))

        line = line[10:].strip()[1:]
        nameAudit = line[:line.find('"')]

        line = line[(line.find('"')+1):].strip()[1:]
        namePrepod = line[:line.find('"')]

        return self(dateCl, nameAudit, namePrepod)

    def getParams(self):
        return [self.date, self.nameAudit, self.namePrepod]

    def __str__(self):
        return f'{self.date} "{self.nameAudit}" "{self.namePrepod}"\n'