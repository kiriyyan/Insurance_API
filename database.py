import psycopg2
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME, DB_PORT

def db_get_client(client_id:int):
    conn = psycopg2.connect(
        host = DB_HOST,
        user = DB_USER,
        password = DB_PASSWORD,
        port = DB_PORT,
        dbname = DB_NAME
    )
    if conn:
        print('DATABASE CONNECTED')

    cursor = conn.cursor()
    sql = f"SELECT * FROM Clients where client_id = %s::INT"
    cursor.execute(sql, (client_id,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result



def db_get_all_clients():
    conn = psycopg2.connect(
        host = "127.0.0.1",
        user = 'postgres',
        password = 'postgres',
        port = 5432,
        dbname = 'insurance'
    )
    if conn:
        print('DATABASE CONNECTED')

    cursor = conn.cursor()
    sql = f"SELECT * FROM Clients"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def db_post_client(first_name, last_name, address, phone_number, email):
    conn = psycopg2.connect(
        host = "127.0.0.1",
        user = 'postgres',
        password = 'postgres',
        port = 5432,
        dbname = 'insurance'
    )
    if conn:
        print('DATABASE CONNECTED')

    cursor = conn.cursor()
    sql = "INSERT INTO clients (first_name, last_name, address, phone_number, email) VALUES(%s, %s, %s, %s, %s)"
    cursor.execute(sql, (first_name,last_name, address, phone_number, email))
    conn.commit()
    cursor.close()
    conn.close()



