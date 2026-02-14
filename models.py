from pydantic import BaseModel, EmailStr, Field

class Client(BaseModel):
    first_name: str =  Field(max_length=64)
    last_name: str =  Field(max_length=64)
    address: str =  Field(max_length=256)
    phone_number: str | None = Field(max_length= 20)
    email: EmailStr