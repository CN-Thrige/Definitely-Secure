from psycopg2 import *

def main():
    show_data()
    
def get_conn():
    return connect(
        host = 'localhost',
        dbname = 'password_vault',
        user = 'postgres',
        password = '1',
        port = 5432
        ) 

def show_data():
    conn = get_conn()
    curr = conn.cursor()

    curr.execute("SELECT * FROM users")

    columns = [desc[0] for desc in curr.description]
    rows = curr.fetchall()

    print(columns)

    for row in rows:
        print(row)

