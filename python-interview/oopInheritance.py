class Course():
  def __init__(self, name:str, maxStudents:int):
    self.name = name
    self.maxStudents = maxStudents
    self.students = []

  def add_student(self, student):
    if len(self.students) < self.maxStudents:
      self.students.append(student)
      return True
    return False  


class Student():
  def __init__(self, name: str, age: int ,grade:int= 100):
    self.name = name
    self.age = age
    self.grade = grade
    pass

  def get_grade(self):
    return self.grade

  def set_grade(self, grade):
    self.grade = grade
    return

s0 = Student("Tim", 15)
s1 = Student("Jessica",16)
s2 = Student("Robin", 15)

course0 = Course("History", 30)
# print(course0.students)
course0.add_student(s0)
print(course0.students[0].name)