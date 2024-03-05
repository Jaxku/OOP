"""
Using Multiple classes and showing how they interact with each other.
"""

# Setting up the sutdent class
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # integer 0-100

    # Method to get the grade
    def get_grade(self):
            return self.grade

# Setting up the course class
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []  # blank list to hold student details

    # Method to add a student to the course
    def add_student(self, student):
        # Test that there is room in the course
        if len(self.students) < self.max_students:
            self.students.append(student)   # add to class if room
            return True     # if student is added successfully
        return False    # if student is not added

    # Method to get average grade
    def get_average_grade(self):
        total = 0
        for student in self.students:
            total += student.get_grade()
        return total / len(self.students)

# instantiate 3 student objects
s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

# print(Student.get_grade(s1))
# print(Student.get_grade(s2))
# print(Student.get_grade(s3))

# Instantiate course object
course1 = Course("Computer Science", 2)

course1.add_student(s1)
course1.add_student(s2)
course1.add_student(s3)

# confirm entry of students
for student in course1.students:
    print(student.name)  # print student names in course1

# Get the average grade of all studnets in a course
print(f"the average grade in {course1.name} is {course1.get_average_grade()}")
