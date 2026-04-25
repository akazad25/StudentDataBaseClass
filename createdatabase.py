class Student:
    def __init__(self, name):
        self.name = name


class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)


s1 = Student("Tanzin")

StudentDatabase.add_student(s1)

for s in StudentDatabase.student_list:
    print(s.name)