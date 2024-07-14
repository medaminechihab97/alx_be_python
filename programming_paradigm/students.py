class Student:
    def __init__ (self,  name,  age):
        self.name = name
        self.age = age
    def get_student_name(self):
        print(f"student name is {self.name}")
        # return name
    def get_student_age(self):
        print(f"student age is {self.age}")
        # return age
    
student1 = Student("chihab", 27)
student1.get_student_name()
student1.get_student_age()
