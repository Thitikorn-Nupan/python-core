# Python Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.

class Info :

    def __init__(self,fullname , age , year):
        # Specify private props
        self.__fullname = fullname
        self.__age = age
        self.__year = year

    def __str__(self):
        return f"(Info) fullname : {self.__fullname} , age : {self.__age} , year : {self.__year}"


# Create a class named Student, which will inherit the properties and methods from the Info class:
class Student(Info) :
    id : int
    code : str
    def __init__(self, id,fullname, age, year):
        ## Python also has a super() function that will make the child class inherit all the methods
        # and properties from its parent:
        ## call __init__(...) on subclass
        super().__init__(fullname, age, year)
        self.id = id
        self.code = "262SDE5959CXZSA" # assume it random
    # I don't need __str__ method because i inherited

    def greeting(self):
        print("Welcome student id",self.id,". Enjoy!!!")


# student = Student(100,"mark ryder",24,4)
## If fullname is not private we can call student.fullname
# print(student.id)
# print(student.code)
# print(student)

# student.greeting()

class StudentService :
    __students : Student
    # Same java can habe multiple construc
    def __init__(self):
        # create list with contruc
        students = list((
            Student(101,"mark ryder",24,4),
            Student(102,"jon ryder",25,3),
            Student(103,"stone ryder",21,2),
        ))
        self.__students = students

    def __init__(self,students):
        self.__students = students

    def getStudents (self) :
        return self.__students


"""
students = StudentService().getStudents()
for student in students:
    # print(student)
    # (Info) fullname : mark ryder , age : 24 , year : 4
    # (Info) fullname : jon ryder , age : 25 , year : 3
    # (Info) fullname : stone ryder , age : 21 , year : 2
    print(student.id) # ** you have to know own what method you called
"""

students = list((
            Student(101,"mark ryder",24,4),
            Student(102,"jon ryder",25,3),
            Student(103,"stone ryder",21,2),
        ))
studentService = StudentService(students)

for student in students:
    print(student)
    # (Info) fullname : mark ryder , age : 24 , year : 4
    # (Info) fullname : jon ryder , age : 25 , year : 3
    # (Info) fullname : stone ryder , age : 21 , year : 2
