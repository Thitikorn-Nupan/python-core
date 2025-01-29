"""
Python Classes/Objects
*** Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.
"""


# Create a class named MyMath, with a property named x,y:

class MyMath:
    """
    Note you don't need to declare prop
    It works like TypeScript
    x = int
    y = int
    """

    # All classes have a function called __init__(), which is always executed when the class is being initiated.
    def __init__(self, x, y):
        # *** Way to called prop. use self.<name prop>
        self.x = x
        self.y = y

    def plusNumbers(self):
        return self.x + self.y

    def plusNumbers(self, x, y, /):  # can not pass argument like (y=5,x=5)
        return x + y

    def plusNumbers(self, x, y):  # can not pass argument like (y=5,x=5)
        return x + y

    # The __str__() function controls what should be returned when the class object is represented as a string.
    def __str__(self):
        return f"x:{self.x} , y:{self.y}"


# Create Object
myMath = MyMath(90, 20)


# print(myMath.plusNumbers()) # error missing 2 required positional arguments: 'x' and 'y'
# print(myMath.plusNumbers(5, 10))  # 30
# print(myMath.plusNumbers(x=5, y=10))  # 30
# # it's like java it'll call __str__ auto
# print(myMath)


## The self parameter is a reference to the current instance of the class,
#  And is used to access variables that belong to the class.
## It does not have to be named self, you can call it whatever you like,
#  But it has to be the first parameter of any function in the class:
# *** All function inside class have to has The self parameter
class Robot:
    # if i want specify type
    id: int
    code: str
    status: bool

    def __init__(objContainProps, id, code, status):
        objContainProps.id = id
        objContainProps.code = code
        objContainProps.status = status
        # print(id) # Now Robot->id is same value id from param

    def changDetail(robot, code, status):
        robot.code = code
        robot.status = status
        return True

    def __str__(objContainProps):
        return f"id:{objContainProps.id},code:{objContainProps.code},status:{objContainProps.status}"


# print(Robot(90,"RT-DAAS6530",True)) # id:1,code:RT-DAAS6530,status:True

robot1 = Robot(100, "GR-93", False)
# robot1.changDetail("FT-965FG",True)
# Or set tru prop
robot1.code = "GB-96SA"
robot1.status = False
# print(robot1) # id:100,code:GB-96SA,status:False

## You can delete objects by using the del keyword:
del robot1


# print(robot1) get error


## The Syntax of Private Methods
## Use a single underscore for “Protected” attributes.
## Use a single underscore for “Protected” attributes.
class Student:
    # private
    __id: int
    __fullname: str
    __age: int

    """    
    # protected
     _id : int
     _fullname : str
     _age : int
     """

    def __init__(studentSelf, id, fullname, age):
        studentSelf.__id = id
        studentSelf.__fullname = fullname
        studentSelf.__age = age

    def getId(studentSelf):
        return studentSelf.__id

    def getFullname(studentSelf):
        return studentSelf.__fullname

    def getAge(studentSelf):
        return studentSelf.__age

    def __str__(studentSelf):
        return f"id:{studentSelf.__id},fullname:{studentSelf.__fullname},age:{studentSelf.__age}"

# print(Student(1001,"alex ryder",23).getId())



