class Student:
    student_list = []

    def __init__(self, student_id, name, department, is_enrolled):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled

        Student.add_student(self)

    @classmethod
    def add_student(cls, student_obj):
        cls.student_list.append(student_obj)

s1 = Student(101, "Tanzin Akter", "CSE", True)
s2 = Student(102, "Halima Akter", "EEE", False)
s3 = Student(103, "Nusrat Jahan", "BBA", True)

for s in Student.student_list:
    print(s.student_id, s.name, s.department, s.is_enrolled)