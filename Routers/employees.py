from fastapi import APIRouter, HTTPException

import database_old
from schemas import Employee

router = APIRouter(prefix ='/Employees', tags = ['Employees'])

@router.get(path = '/', summary = 'Get employees list', status_code=200)
def get_all_employees():
    try:
        employees_list = database.db_get_all_employees()
        return employees_list
    except:
        raise HTTPException(status_code=500, detail='database_error')

@router.get(path = '/{employee_id}', summary= 'Get employee by id', status_code=200)
def get_employee(employee_id:int):
    try:
        employee = database.db_get_employee(employee_id)
    except:
        raise HTTPException(status_code=500, detail='database_error')
    if employee:
        return employee
    else:
        raise HTTPException(status_code=404, detail = 'employee not found')

@router.post(path = '/', summary='Create a new employee', status_code=201)
def create_employee(new_employee: Employee):
    try:
        employee = database.db_post_employee(
            first_name = new_employee.first_name,
            last_name = new_employee.last_name,
            phone_number = new_employee.phone_number,
            department_id = new_employee.department_id)
        return {'status': 'created', 'id': employee}
    except:
        raise HTTPException(status_code=500, detail='database_error')

