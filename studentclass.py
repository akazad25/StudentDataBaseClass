class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled
     

student1 = Student(101, "Tanzin", "CSE", True)

print(student1.student_id)
print(student1.name)
print(student1.department)
print(student1.is_enrolled)