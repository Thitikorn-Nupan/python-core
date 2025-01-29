from pratice_oop.entity.student import Student # way to import class


class ServiceStudent :
    # Define a list with type
    __students : list[Student]
    def __init__(self):
        # create list with constructor
        students = list((
            Student(101, "mark"," ryder", 24),
            Student(102, "jon","bones", 25),
            Student(103, "stone", "slider", 21),
        ))
        self.__students = students

    def getStudents(self):
        return self.__students


    def getStudent(self,id):
        for studentHold in self.__students :
            if studentHold.getId() == id :
                # Found
                return True
        # Not found
        return False

    def removeStudent(self,id):
        for studentHold in self.__students :
            if studentHold.getId() == id :
                # # List Comprehension ****
                # Update List
                self.__students = [student for student in self.__students if student.getId() != id]
                return True
        # Not found
        return False

    def editStudent(self,student,id):
        for studentHold in self.__students :
            if studentHold.getId() == id :
                # # List Comprehension ****
                # Update List
                studentHold.setFirstname(student.getFirstname())
                studentHold.setLastname(student.getLastname())
                studentHold.setAge(student.getAge())
                return True
        # Not found
        return False