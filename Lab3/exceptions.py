class LessonError(Exception):
    pass


class InvalidDateError(LessonError):
    pass


class EmptyAuditError(LessonError):
    pass


class EmptyPrepodError(LessonError):
    pass


class FormatError(LessonError):
    pass