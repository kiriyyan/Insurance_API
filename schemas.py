from pydantic import BaseModel, EmailStr, Field, condecimal
from decimal import Decimal
from datetime import date
from enum import Enum

class Client(BaseModel):
    first_name: str =  Field(max_length=64)
    last_name: str =  Field(max_length=64)
    address: str =  Field(max_length=256)
    phone_number: str = Field(max_length= 20)
    email: EmailStr = Field(max_length = 128)

class Department(BaseModel):
    name: str = Field(max_length=128)
    address: str = Field(max_length=256)
    phone_number: str = Field(max_length=20)

class Employee(BaseModel):
    first_name: str = Field(max_length=64)
    last_name: str = Field(max_length=64)
    phone_number: str = Field(max_length=20)
    department_id: int

class ContractStatus(str, Enum):
    ACTIVE = "active"
    EXPIRED = "expired"
    CANCELLED = "cancelled"

class Contract(BaseModel):
    status: ContractStatus
    start_date: date | None
    end_date: date
    coverage_amount: condecimal(max_digits=15, decimal_places=2)
    premium_amount: condecimal(max_digits=15, decimal_places=2)
    policy_type: str = Field(max_length=128)
    client_id:int
    employee_id:int