import json

class Student :

    def __init__(self,id : int,fullname : str):
        self.id = id
        self.fullname = fullname

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda student : student.__dict__,
            )
