import json


class Student:
    def getStudents(self):
        mockStudent = dict({"name": "mani", "rolNo": 1001})
        return json.dumps(mockStudent, indent=4)

    def insertStudent(self, request):
        print("entered into post method Student class method")
        print(request)
        return {"data": str(1) + "record inserted"}
