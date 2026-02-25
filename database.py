from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text, insert
import asyncio

from models import employees_model, departments_model, clients_model, contracts_model
from config import settings

async_engine = create_async_engine(
    url = settings.DATABASE_URL_asyncpg,
    echo = True

)

async def get_info():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT * FROM clients"))
        print(f'------------------------{res.fetchall()}')

async def insert_data_text():
    async with async_engine.connect() as conn:
        stmt = '''INSERT INTO department(name, address, phone_number) VALUES('orm', 'qwerqe', '228')
        '''
        await conn.execute(text(stmt))
        await conn.commit()


async def insert_data():
    async with async_engine.connect() as conn:
        stmt =insert(departments_model).values([
            {'name': 'OGO RABOTAET',
             'address': 'WOW',
             'phone_number': '1234124513'}
        ])
        await conn.execute(stmt)
        await conn.commit()

asyncio.run(insert_data())