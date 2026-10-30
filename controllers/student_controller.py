from fastapi import APIRouter, Response
from models.student_model import Student

# Localy store in memory data
students = []
id = 0

# create student 

def create_student(student: Student, response: Response):
    global id
    try:
        id += 1
        student.id = id
        students.append(student)
        response.status_code = 201
        return {'isSuccess': True, 'message': 'Student created successfully', 'student': student}
    except Exception as e:
        response.status_code = 500
        return {'isSuccess': False, 'message': str(e), 'student': None}


# read all students
def get_all_students(response: Response):
    try:
        response.status_code = 200
        return {'isSuccess': True, 'message': 'Students fetched successfully', 'student': students}
    except Exception as e:
        response.status_code = 500
        return {'isSuccess': False, 'message': str(e), 'student': None}

# read student by id
def get_student_by_id(studentid: int, response: Response):
    try:
        response.status_code = 200
        for student in students:
            if student.id == studentid:
                return {'isSuccess': True, 'student': student}

        response.status_code = 404
        return {'isSuccess':False, 'message' : 'Student not found'}
    except Exception as e:
        print(e)
        response.status_code = 500
        return{'isSuccess' : False, 'message' : str(e)}

# update student by id
def update_student(studentid: int, updated_student: Student, response: Response):
    try:
        response.status_code = 200
        for student in students:
            if student.id == studentid:
                student.name = updated_student.name
                student.course = updated_student.course
                student.marks = updated_student.marks

                return {'isSuccess': True, 'message': 'Student Updated Successfully', 'student': student}

        response.status_code = 404
        return {'isSuccess': False, 'message': 'Student not found'}

    except Exception as e:
        response.status_code = 500
        return {'isSuccess': False, 'message': str(e)}


# delete student by id
def delete_student(studentid: int, response: Response):
    try:
        response.status_code = 200
        for student in students:
            if student.id == studentid:
                students.remove(student)
                return {'isSuccess': True, 'message': 'Student deleted successfully', 'student': student}

        response.status_code = 404
        return {'isSuccess': False, 'message': 'Student not found'}

    except Exception as e:
        response.status_code = 500
        return {'isSuccess': False, 'message': str(e)}

