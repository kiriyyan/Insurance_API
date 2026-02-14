#uvicorn main:app --reload

import uvicorn
from fastapi import FastAPI, HTTPException
import json


from models import Client
from Mock_clients import clients

app = FastAPI()

@app.get('/clients',tags = ['Clients'], summary="Даёт список клиентов")
def get_clients():
    if clients:
        return json.dumps(clients)
    else:
        raise HTTPException(status_code=400,detail="Недоступен список клиентов")

@app.get('/clients/{client_id}',tags = ['Clients'], summary="Даёт клиента по Client_id")
def get_client(client_id:int):
    for n in clients:
        if int(n['client_id']) == client_id:
            return n
    raise HTTPException(status_code=404,detail="Клиент не найден")


@app.post('/clients')
def create_client(new_client: Client):
    clients.append({
        'client_id': len(clients) ,
        'first_name': new_client.first_name,
        'last_name': new_client.last_name,
        'address': new_client.address,
        'phone_number': new_client.phone_number,
        'email': new_client.email,
    })
    return {'status':'ok'}

if __name__ == '__main__':
    uvicorn.run(app, reload = True)

