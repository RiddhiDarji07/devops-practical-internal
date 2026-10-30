from fastapi import APIRouter, FastAPI, Response
from models.student_model import Student
from controllers.student_controller import create_student, get_all_students, get_student_by_id, update_student, delete_student

StudentRouter = APIRouter(
    prefix= '/students',
    tags= ['students']
)


# create student -
@StudentRouter.post('/')
def create_student_route(student: Student, response: Response):
    return create_student(student, response)

# read all students
@StudentRouter.get('/')
def get_all_students_route(response: Response):
    return get_all_students(response)

# read student by id
@StudentRouter.get('/{studentid}')
def get_student_by_id_route(studentid: int, response: Response):
    return get_student_by_id(studentid, response)

# update student by id
@StudentRouter.put('/{studentid}')
def update_student_route(studentid: int, updated_student: Student, response: Response):
    return update_student(studentid, updated_student, response)

# delete student by id
@StudentRouter.delete('/{studentid}')
def delete_student_route(studentid: int, response: Response):
    return delete_student(studentid, response)


