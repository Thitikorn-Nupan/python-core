import datetime
from glob import escape
from model.student import Student
from flask import Flask, jsonify, request  # Flask library for build apis
import json # import required packages
from log import log_application

logApplication = log_application.LogApplication(__file__)
log = logApplication.log
app = Flask(__name__)

@app.route('/date.day', methods=['GET'])
def getDateToDay():
    result = datetime.date.today().day
    return jsonify({'date': result})


@app.route('/date.year', methods=['GET'])
def getDateYear():
    result = datetime.date.today().year
    return {'date':result} # as a json too

"""
Variable Rules
You can add variable sections to a URL by marking sections with <variable_name>. 
Your function then receives the <variable_name> as a keyword argument. 
Optionally, you can use a converter to specify the type of the argument like <converter:variable_name>
"""
@app.route('/message/<str>', methods=['GET'])
def getMessageHasPathVariable(str): # str map str
    return {'message': str} # as a json too

#  you can use a converter to specify the type of the argument like <converter:variable_name>
@app.route('/plus/<int:a>/<int:b>', methods=['GET'])
def getPlus(a:int,b:int): # str map str
    return {'plus': F"{a} + {b} = {a+b}"} # as a json too

@app.route('/path/<path:subpath>') # like string but also accepts slashes
def showSubPath(subpath):
    return F"Sub path is {escape(subpath)}"

## Test Collect with API
def getStudentsAsList () :
    s1 = Student(1, 'Alex Ryder')
    s2 = Student(2, 'Alex Slider')
    s3 = Student(3, 'Alex Owner')
    students = list((s1.__dict__, s2.__dict__, s3.__dict__))
    return students
@app.route('/student/<option>',methods=['GET'])
def showStudent(option:str):
    # object1,2 same result
    # request.method is once of flask library
    if option == 'object1' and request.method == 'GET':
        return json.dumps(Student(1,'Alex Ryder').__dict__)
        """
        {
            "id": 1,
            "fullname": "Alex Ryder"
        }   
        """
    elif option == 'object2' :
        student = Student(1,'Alex Ryder')
        log.debug(student.toJSON()) # {"id": 1, "fullname": "Alex Ryder"}
        log.debug(student.__dict__) # {'id': 1, 'fullname': 'Alex Ryder'} it work as __str__ so you don't need to create __str__ on own!
        log.debug(student.__dict__.get('fullname')) # Alex Ryder
        return student.toJSON()

    ### Note json.dumps(...) or jsonify(...) work for covert data to json format
    elif option == 'list1' :
        s1 = Student(1,'Alex Ryder')
        s2 = Student(2,'Alex Slider')
        s3 = Student(3,'Alex Owner')
        students = list()
        students.insert(0,s1.__dict__)
        students.insert(1,s2.__dict__)
        students.insert(2,s3.__dict__)
        """
        Note. format list should be like be low 
        list = [
            {'a': 1, 'b': 2},
            {'a': 5, 'b': 10}
        ]
        """
        log.debug("students %s",students) #  students [{'id': 1, 'fullname': 'Alex Ryder'}, {'id': 2, 'fullname': 'Alex Slider'}, {'id': 3, 'fullname': 'Alex Owner'}]
        return jsonify(students)
        """
        [
            {
                "fullname": "Alex Ryder",
                "id": 1
            },
            
            {
                "fullname": "Alex Slider",
                "id": 2
            },
            
            {
                "fullname": "Alex Owner",
                "id": 3
            }
        ]
        """
    elif option == 'list2':
        students = getStudentsAsList()
        log.debug("students %s",students)  #
        return jsonify(students) # same list1

    elif option == 'list3':
        students = getStudentsAsList()
        log.debug("students %s",students)   # ['{"id": 1, "fullname": "Alex Ryder"}']
        return json.dumps(students) # same list1

    # We can get parameter using request.args.get('<name>')
    elif option == 'list4' and request.args.get('code') == 'list4': ## endpoint look like this /student/list4?code=list4
        students = getStudentsAsList()
        log.debug("students %s",students) #
        return json.dumps(students)  # same list1



if __name__ == '__main__':
    app.run(host='localhost',port=8083)