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

    def enroll_student(self):
        if self.is_enrolled:
            print(f"{self.name} is already enrolled.")
        else:
            self.is_enrolled = True
            print(f"{self.name} has been enrolled successfully.")

s1 = Student(101, "Tanzin Akter", "CSE", False)

s1.enroll_student()
