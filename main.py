#uvicorn main:app --reload

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Routers import clients, contracts, departments, employees

app = FastAPI()
app.include_router(clients.router)
app.include_router(contracts.router)
app.include_router(departments.router)
app.include_router(employees.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run(app, reload = True)

