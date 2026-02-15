from fastapi import APIRouter, HTTPException

import database
from models import Department


router = APIRouter(prefix ='/Departments', tags = ['Departments'])

@router.get(path='/', summary='Get departments list', status_code=200)
def get_departments():
    try:
        department_list = database.db_get_all_departments()
        return department_list
    except Exception as e:
        raise HTTPException(500, detail='database_error')

@router.get(path = '/{department_id}', summary='Get department by id', status_code=200)
def get_department(department_id:int):
    try:
        department = database.db_get_department(department_id)
    except:
        raise HTTPException(status_code=500, detail='database_error')
    if department:
        return department
    else:
        raise HTTPException(status_code=404, detail = 'department not found')

@router.post(path='/', summary = 'Create a new department', status_code=201)
def create_department(new_department: Department):
    try:
        department = database.db_post_department(name = new_department.name, address = new_department.address, phone_number = new_department.phone_number)
        return {'status': 'created', 'id': department}
    except:
        raise HTTPException(500, 'database_error')