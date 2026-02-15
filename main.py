#uvicorn main:app --reload

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


from models import Client, Department

import database



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/clients',tags = ['Clients'], summary="Get full client list", status_code=200)
def get_clients():
    try:
        clients = database.db_get_all_clients()
        return clients
    except Exception as e:
        raise HTTPException(status_code=500, detail='database_error')

@app.get('/clients/{client_id}',tags = ['Clients'], summary="Get client by id", status_code=200)
def get_client(client_id:int):
    try:
        client = database.db_get_client(client_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail='database_error')
    if client:
        return client
    else:
        raise HTTPException(status_code=404, detail='Client not found')

@app.post('/clients', tags = ['Clients'], summary="Create a new client", status_code=201)
def create_client(new_client: Client):
    try:
        current_client = database.db_post_client(new_client.first_name, new_client.last_name, new_client.address, new_client.phone_number, new_client.email)
        return {'status':'created', 'id': current_client}
    except Exception as e:
        raise HTTPException(500, detail='database_error')


@app.get(path='/departments', tags=['Departments'], summary='Get departments list', status_code=200)
def get_departments():
    try:
        department_list = database.db_get_all_departments()
        return department_list
    except Exception as e:
        raise HTTPException(500, detail='database_error')

@app.get(path = '/departments/{department_id}', tags=['Departments'], summary='Get department by id', status_code=200)
def get_department(department_id:int):
    try:
        department = database.db_get_department(department_id)
    except:
        raise HTTPException(status_code=500, detail='database_error')
    if department:
        return department
    else:
        raise HTTPException(status_code=404, detail = 'department not found')

@app.post(path='/departments',tags=['Departments'], summary = 'Create a new department', status_code=201)
def create_department(new_department: Department):
    try:
        department = database.db_post_department(name = new_department.name, address = new_department.address, phone_number = new_department.phone_number)
        return {'status': 'created', 'id': department}
    except:
        raise HTTPException(500, 'database_error')


if __name__ == '__main__':
    uvicorn.run(app, reload = True)

