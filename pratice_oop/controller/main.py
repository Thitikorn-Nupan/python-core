from pratice_oop.service.service_student import ServiceStudent

class StudentControl:

    __studentService: ServiceStudent

    def __init__(self):
        self.__studentService = ServiceStudent()

    ## Crud logic
    def reads(self):
        for student in self.__studentService.getStudents():
            print(student)
    def read(self, id):
        print(self.__studentService.getStudent(id))
    def delete(self, id):
        print(self.__studentService.removeStudent(id))

    def update(self, student, id):
        print(self.__studentService.editStudent(student, id))


studentControl = StudentControl()

# StudentControl().reads()
# StudentControl().read(109)
# StudentControl().delete(101)

# studentControl.delete(101)
# studentControl.delete(105)
# studentControl.reads()

# studentControl.reads()
# student = Student(0,"adam","sandler",35)
# studentControl.update(student,103)
# studentControl.reads()
