#uvicorn main:app --reload

import uvicorn
from fastapi import FastAPI, HTTPException



from models import Client

import database

app = FastAPI()

@app.get('/clients',tags = ['Clients'], summary="Даёт список клиентов")
def get_clients():
    try:
        return database.db_get_all_clients()
    except Exception as e:
        return {'status': e}

@app.get('/clients/{client_id}',tags = ['Clients'], summary="Даёт клиента по Client_id")
def get_client(client_id:int):
    try:
        return database.db_get_client(client_id)
    except Exception as e:
        return {'status': e}
    # raise HTTPException(status_code=404,detail="Клиент не найден")


@app.post('/clients')
def create_client(new_client: Client):
    try:
        database.db_post_client(new_client.first_name, new_client.last_name, new_client.address, new_client.phone_number, new_client.email)
        return {'status':'ok'}
    except Exception as e:
        return {'status':e}

if __name__ == '__main__':
    uvicorn.run(app, reload = True)

