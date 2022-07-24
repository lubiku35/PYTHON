from abc import ABC, abstractmethod

class Person(ABC):
   def __init__(self, name, surname):
      self.name = name
      self.surname = surname

   @abstractmethod
   def introduce_yourself(self):
      pass
      

class Student(Person):
   def __init__(self, name, surname, grade):
      # dedenie z rodičovského konštruktoru Person
      super().__init__(name, surname)
      self.grade = grade
      
   def introduce_yourself(self):
      print(f"Hi my name is {self.name} and surname is {self.surname}")

   def __str__(self):
      return f"Student -> name: {self.name} surname: {self.surname} grade: {self.grade}"

class Teacher(Person):
   def __init__(self, name, surname, degree):
      # dedenie z rodičovského konštruktoru Person
      super().__init__(name, surname)
      self.degree = degree
      
   def introduce_yourself(self):
      print(f"Hi my name is {self.name} and surname is {self.surname} and I'm teacher")

   def __str__(self):
      return f"Teacher -> name: {self.name} surname: {self.surname} degree: {self.degree}"
        






#student1 = Student("Ľuboš", "Motošický", 3)
#student2 = Student("Michal", "Davidák", 8)
#teacher = Teacher("Lucas", "White", "Mgr")
#print(teacher)
#course = Course("Math", teacher, [student1, student2])
#print(course)

