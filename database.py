import psycopg2
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME, DB_PORT

def db_connection(func):
    def wrapper(*args, **kwargs):
        conn = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT,
            dbname=DB_NAME
        )
        if conn:
            print('DATABASE CONNECTED')
        cursor = conn.cursor()

        try:
            result = func(cursor, conn, *args, **kwargs)
            conn.commit()
            return result
        except Exception as e:
            print(e)
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()

    return wrapper

@db_connection
def db_get_client(cursor, conn, client_id:int):
    sql = f"SELECT * FROM Clients where client_id = %s::INT"
    cursor.execute(sql, (client_id,))
    result = cursor.fetchone()

    return result


@db_connection
def db_get_all_clients(cursor, conn):
    sql = f"SELECT * FROM Clients"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

@db_connection
def db_post_client(cursor, conn, first_name, last_name, address, phone_number, email):
    sql = "INSERT INTO clients (first_name, last_name, address, phone_number, email) VALUES(%s, %s, %s, %s, %s) RETURNING client_id"
    cursor.execute(sql, (first_name,last_name, address, phone_number, email))
    return cursor.fetchone()[0]

@db_connection
def db_get_all_departments(cursor, conn):
    sql = "SELECT * FROM department"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

@db_connection
def db_get_department(cursor,conn,department_id):
    sql = "SELECT * FROM department WHERE department_id = %s"
    cursor.execute(sql, (department_id,))
    result = cursor.fetchone()
    return result

@db_connection
def db_post_department(cursor,conn,name,address,phone_number):
    sql = "INSERT INTO department(name, address,phone_number) VALUES(%s, %s, %s) RETURNING department_id"
    cursor.execute(sql, (name, address, phone_number))
    result = cursor.fetchone()[0]
    return result


