class Student :

    __id : int
    __firstname : str
    __lastname : str
    __age : int

    def __init__(self,id,firstname,lastname,age):
        self.__id = id
        self.__firstname = firstname
        self.__lastname = lastname
        self.__age = age

    """
    def __init__(self):
        self.__id = 1
        self.__firstname = "test"
        self.__lastname = "test"
        self.__age = 1
    """

    def getId(self):
        return self.__id

    def getFirstname(self):
        return self.__firstname

    def getLastname(self):
        return self.__lastname

    def setFirstname(self,firstname):
        self.__firstname = firstname

    def setLastname(self,lastname):
        self.__lastname = lastname

    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age

    def __str__(self):
        return f"id : {self.__id} , fullname : {self.__firstname} {self.__lastname} , age : {self.__age}"


