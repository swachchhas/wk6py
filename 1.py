class Student:
    def __init__(self, name, age, grades):
        self.name = name  
        self.age = age    
        self.grades = grades  

    def average_grade(self):  
        return sum(self.grades) / len(self.grades)


student1 = Student("Alice", 20, [85, 90, 78, 92, 88])
student2 = Student("Bob", 22, [75, 80, 82, 85, 78])
student3 = Student("Charlie", 21, [90, 95, 89, 92, 94])


print(f"{student1.name}'s average grade: {student1.average_grade()}")
print(f"{student2.name}'s average grade: {student2.average_grade()}")
print(f"{student3.name}'s average grade: {student3.average_grade()}")
