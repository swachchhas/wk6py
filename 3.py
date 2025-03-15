class StudentResult:
    def __init__(self, name, age, average_grade):
        self.name = name
        self.age = age
        self.average_grade = average_grade

    def has_passed(self):
        return self.average_grade >= 50

student1 = StudentResult("Alice", 20, 75)
student2 = StudentResult("Bob", 22, 45)
student3 = StudentResult("Charlie", 21, 60)

for student in [student1, student2, student3]:
    if student.has_passed():
        print(f"{student.name} has passed.")
