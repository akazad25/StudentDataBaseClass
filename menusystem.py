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

    def drop_student(self):
        if not self.is_enrolled:
            print(f"{self.name} is already not enrolled.")
        else:
            self.is_enrolled = False
            print(f"{self.name} has dropped out successfully.")

    def view_student_info(self):
        status = "Enrolled" if self.is_enrolled else "Not Enrolled"
        print(f"{self.student_id} | {self.name} | {self.department} | {status}")


# ---------------- MENU SYSTEM ---------------- #

def find_student(student_id):
    for student in Student.student_list:
        if student.student_id == student_id:
            return student
    return None


# Sample data (you can add manually too)
Student(101, "Rahim Uddin", "CSE", True)
Student(102, "Karim Khan", "EEE", False)
Student(103, "Nusrat Jahan", "BBA", True)


while True:
    print("\n===== STUDENT MENU =====")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n--- All Students ---")
        for s in Student.student_list:
            s.view_student_info()

    elif choice == "2":
        sid = int(input("Enter Student ID to enroll: "))
        student = find_student(sid)
        if student:
            student.enroll_student()
        else:
            print("Student not found.")

    elif choice == "3":
        sid = int(input("Enter Student ID to drop: "))
        student = find_student(sid)
        if student:
            student.drop_student()
        else:
            print("Student not found.")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")