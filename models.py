from pydantic import BaseModel, EmailStr, Field, condecimal
from decimal import Decimal

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