#uvicorn main:app --reload

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


from models import Client

import database



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/clients',tags = ['Clients'], summary="Даёт список клиентов")
def get_clients():
    try:
        clients = database.db_get_all_clients()
        return clients
    except Exception as e:
        raise HTTPException(status_code=500, detail='database_error')

@app.get('/clients/{client_id}',tags = ['Clients'], summary="Даёт клиента по Client_id")
def get_client(client_id:int):
    try:
        client = database.db_get_client(client_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail='database_error')
    if client:
        return client
    else:
        raise HTTPException(status_code=404, detail='Client not found')



@app.post('/clients', tags = ['Clients'], summary="Создаёт нового клиента", status_code=201)
def create_client(new_client: Client):
    try:
        current_client = database.db_post_client(new_client.first_name, new_client.last_name, new_client.address, new_client.phone_number, new_client.email)
        return {'status':'ok', 'id': current_client}
    except Exception as e:
        raise HTTPException(500, detail='database_error')


if __name__ == '__main__':
    uvicorn.run(app, reload = True)

