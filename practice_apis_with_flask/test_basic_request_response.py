from http import HTTPStatus
from flask import Flask, jsonify, request  # Flask library for build apis

from log import log_application as fileLog
from practice_apis_with_flask.model.student import Student

logApplication = fileLog.LogApplication(__file__)
log = logApplication.log
app = Flask(__name__)

# log.debug("test %s",12) # all data you want to log have to put %s , <data>
# test communicate http as json type with backend api

__baseUrl = "/api/user"


class StudentService:

    def __init__(self):
        s1 = Student(1, 'Alex Ryder')
        s2 = Student(2, 'Alex Slider')
        s3 = Student(3, 'Alex Owner')
        # __dir__ func is importance for response api
        self.students: list[Student] = list((s1.__dict__, s2.__dict__, s3.__dict__))

    def create(self, student: Student):
        size = len(self.students)  # get size ** it starts 1
        log.debug("students size %s", size)
        self.students.insert(size,
                             student.__dict__)  # don't forget keep format! if you don't specify __dict__ your last item is  object <practice_apis_with_flask.model.student.Student object at 0x0000020AFEB26150>
        nSize = len(self.students)
        return size is not nSize

    # end class

    def read(self, id: int):
        for student in self.students:
            # if you get error about attributes! Instead of using task.id you should use task['id']
            # log.debug("student %s", student['id'])
            if student['id'] == id :
                log.debug("student %s", student)
                return student # it returns as student.__dict__ because i set it ** self.students: list[Student] = list((s1.__dict__, s2.__dict__, s3.__dict__))
        return Student(0,'').__dict__ # but this if i don't specify .__dict__ will get error cause it's not json


"""def reads(self):
    return self.students"""

studentService = StudentService()


# log.debug(studentService.create(Student(4, 'Alex Swong')))

@app.route(__baseUrl + "/create", methods=['POST'])
def saveUser():
    log.debug("request.form %s , request.json %s", request.form,
              request.json)  # request.form ImmutableMultiDict([]) , request.json {'username': 'admin', 'password': '12345'}
    id = request.json['id']
    fullname = request.json['fullname']
    student = Student(id, fullname)
    # log.debug("student %s",student.__dict__)

    return jsonify({'status': HTTPStatus.CREATED,
                    'data': studentService.create(student)
                    }), HTTPStatus.CREATED  # you can change response http status


# can have multiple routes on a function
# this endpoint look like user/ , user/reads
@app.route(__baseUrl + "/reads", methods=['GET'])
@app.route(__baseUrl + "/", methods=['GET'])
def fetchAllStudents():
    # students = studentService.reads()
    # log.debug("students %s",students)
    return jsonify({
        'status': HTTPStatus.OK,
        'data': studentService.students
    }), HTTPStatus.OK


@app.route(__baseUrl + "/read", methods=['GET'])
def fetchStudent():
    id = int(request.args.get('id'))  # get parameter on uri
    log.debug("id %s", id)
    return jsonify({'status': HTTPStatus.OK,
                    # 'data' : Student(id, 'Alex Owner').__dict__ #.__dir__ return json format
                    'data': studentService.read(id)
                    }), HTTPStatus.OK


app.run(host='localhost', port=8083)
