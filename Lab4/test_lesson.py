import unittest
from datetime import date
from lesson import Lesson
from exceptions import InvalidDateError, EmptyAuditError, EmptyPrepodError, FormatError

class TestLesson(unittest.TestCase):

    def test_correct_init(self):
        raw = '2023-10-25 "404" "Илюша"'
        obj = Lesson.initLesson(raw)
        self.assertEqual(obj.nameAudit, "404")
        self.assertEqual(obj.namePrepod, "Илюша")
        self.assertEqual(obj.date, date(2023, 10, 25))

    def test_broken_date(self):
        with self.assertRaises(InvalidDateError):
            Lesson.initLesson('2023-99-99 "404" "Илюша"')

    def test_missing_quotes_audit(self):
        with self.assertRaises(FormatError) as context:
            Lesson.initLesson('2023-10-25 123 "Илюша"')

    def test_missing_quotes_prepod(self):
        with self.assertRaises(FormatError) as context:
            Lesson.initLesson('2023-10-25 "123" Илюша')

    def test_missing_audit(self):
        with self.assertRaises(EmptyAuditError):
            Lesson.initLesson('2023-10-25 "" "Илюша"')
    

    def test_missingyy(self):
        raw = '2023-10-25 "404" "Илюша"'
        obj = Lesson.initLesson(raw)
        params = obj.getParams()
        self.assertEqual(params[0], date(2023, 10, 25))
        self.assertEqual(params[1], "404")
        self.assertEqual(params[2], "Илюша")
    


if __name__ == '__main__':
    unittest.main()