class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def validatedetails(self):
        if len(self.student_id) != 7 or self.student_id[:3] != "STU" or not self.student_id[3:].isdigit():
            return "Invalid student ID. Must be in the format STU1234."
        if len(self.name) < 2 or not all(char.isalpha() or char == " " for char in self.name):
            return "Invalid name. Must be at least 2 characters and only contain letters and spaces."
        if not (self.grade.endswith(" Grade") and self.grade[:-6].isdigit() and 1 <= int(self.grade[:-6]) <= 12):
            return "Invalid grade. Must be like '1st Grade' to '12th Grade'."

        return "Details are valid."
    
    def display_details(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade}")

student1 = Student("STU1234", "Alice", "10th Grade")
result = student1.validatedetails()
print(result)
if result == "Details are valid.":
    student1.display_details()
