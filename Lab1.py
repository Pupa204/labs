from datetime import date

class Lesson():
  def __init__(self, data: date, nameAudit: str, namePrepod: str, TypeAudit: str):
    self.data = data
    self.nameAudit = nameAudit
    self.namePrepod = namePrepod
    self.TypeAudit = TypeAudit


  def __str__(self):
    return (
            f"Дата: {self.data}\n"
            f"Аудитория: {self.nameAudit}\n"
            f"Имя: {self.namePrepod}\n"
            f"Тип аудитории: {self.TypeAudit} "
        )

def getParam(line):
  line = line.strip()
  data_Y, date_m, date_d = line[:10].split(".")
  data = date(int(data_Y), int(date_m), int(date_d))

  line = line[10:].strip()[1:]
  nameAudit = line[:line.find('"')]

  line = line[(line.find('"')+1):].strip()[1:]
  namePrepod = line[:line.find('"')]

  line = line[(line.find('"')+1):].strip()[1:]
  TypeAudit = line[:line.find('"')]

  return Lesson(data, nameAudit, namePrepod, TypeAudit)


line = '2025.10.15 "513" "Антон" "A"'

less = getParam(line)
print(less)