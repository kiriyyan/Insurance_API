from fastapi import APIRouter, HTTPException

import database
from models import Contract


router = APIRouter(prefix ='/Contracts', tags = ['Contracts'])

@router.get(path = '/', summary = 'Get contracts list', status_code=200)
def get_contracts():
    try:
        contracts_list = database.db_get_all_contracts()
        return contracts_list
    except:
        raise HTTPException(status_code=500, detail='database_error')

@router.get(path = '/{contract_id}', summary = 'Get contract by id', status_code=200)
def get_contract(contract_id:int):
    try:
        contract = database.db_get_contract(contract_id = contract_id)
    except:
        raise HTTPException(status_code=500, detail='database_error')
    if contract:
        return contract
    else:
        raise HTTPException(status_code=404, detail='contract not found')

@router.post(path = '/', summary = 'Create a new contract', status_code=201)
def create_contract(new_contract: Contract):
    try:
        contract_id = database.db_post_contract(coverage_amount = new_contract.coverage_amount,
                                                premium_amount = new_contract.premium_amount,
                                                status = new_contract.status,
                                                end_date = new_contract.end_date,
                                                start_date = new_contract.start_date,
                                                client_id = new_contract.client_id,
                                                employee_id = new_contract.employee_id,
                                                policy_type = new_contract.policy_type)
        return contract_id
    except:
        raise HTTPException(status_code=500, detail='database_error')