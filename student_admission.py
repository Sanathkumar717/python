class Student:
    def __init__(self):
        self.__sid=None
        self.__age=None
        self.__marks=None
    def validate_marks(self):
        return self.__marks>=0 and self.__marks<=100
         
    def validate_age(self):
        return self.__age>20
    def check_qualification(self):
        if self.validate_marks() and self.validate_age():
            return self.__marks>=65
        else:
            return False
    def setter(self):
        self.__sid=input("enter student_id: ")
        self.__age=int(input("age: "))
        self.__marks=int(input("marks: "))
    def getter(self):
        print("Student_id: ",self.__sid,"\nAge: ",self.__age,"\nMarks: ",self.__marks)
n=int(input("enter number of students: "))
Studs=[]
for i in range(n):
    Studs.append(Student())
for i in range(n):
    Studs[i].setter()
    Studs[i].getter()
    print("qualified: ",Studs[i].check_qualification())
    print()
