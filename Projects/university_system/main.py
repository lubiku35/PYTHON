from information_system import InformationSystem
from personal import Teacher
from course import Course

def print_menu():
   print("\n*********************************")
   print("Welcome to the Information System\n")
   print("Please choose from above:")
   print("\t[0] -> Add Teacher")
   print("\t[1] -> Add Course")
   print("\t[2] -> Add Student")
   print("\t[3] -> List of Teachers")
   print("\t[4] -> List of Courses")
   print("\t[5] -> List of Students")
   print("\t[6] -> Exit System")

in_sys = InformationSystem(
   teachers= [
      Teacher("Lucas", "White", "Mgr"),
      Teacher("David", "Blue", "Ing"),
      Teacher("Elene", "Black", "Ing"),
      Teacher("Andrew", "Purple", "Mgr"),
      Teacher("Kai", "Dark", "Phd"),
      Teacher("Michael", "Brown", "Ing"),
      Teacher("Samuel", "Yellow", "Phd"),
      Teacher("Sona", "Pink", "Mgr"),
   ],
   courses= [
      Course("Math"),
      Course("IT"),
      Course("Psychology"),
      Course("Biology"),
      Course("Chemistry"),
      Course("IT++")
   ]
)

while True:
   print_menu()
   try:
      menu_choice = int(input("Menu choice: "))
      if menu_choice < 0 or menu_choice >= 7:
         raise Exception("Wrong menu choice")
   except Exception as e:
      print(e)
      print("Please choose valid menu choice")
      continue
   if menu_choice == 6:
      print("Goodbye...")
      break
   elif menu_choice == 0:
      in_sys.create_teacher()
   elif menu_choice == 1:
      in_sys.create_course()
   elif menu_choice == 2:
      in_sys.create_student()
   elif menu_choice == 3:
      print("Courses are:")
      for course in in_sys.courses:
         print(course)
   elif menu_choice == 4:
      print("Students are:")
      for student in in_sys.students:
         print(student)
   elif menu_choice == 5:
      print("Teachers are")
      for teacher in in_sys.teachers:
         print(teacher)
       