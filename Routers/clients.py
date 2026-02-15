import database
from models import Client
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix ='/clients', tags = ['Clients'])

@router.get('/', summary="Get full client list", status_code=200)
def get_clients():
    try:
        clients = database.db_get_all_clients()
        return clients
    except Exception as e:
        raise HTTPException(status_code=500, detail='database_error')

@router.get('/{client_id}', summary="Get client by id", status_code=200)
def get_client(client_id:int):
    try:
        client = database.db_get_client(client_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail='database_error')
    if client:
        return client
    else:
        raise HTTPException(status_code=404, detail='Client not found')

@router.post('/', summary="Create a new client", status_code=201)
def create_client(new_client: Client):
    try:
        current_client = database.db_post_client(new_client.first_name, new_client.last_name, new_client.address, new_client.phone_number, new_client.email)
        return {'status':'created', 'id': current_client}
    except Exception as e:
        raise HTTPException(500, detail='database_error')