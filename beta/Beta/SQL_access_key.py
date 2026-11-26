from psycopg2 import *


def get_conn(): #accesing the sql-server
    return connect(
        host = 'localhost',
        dbname = 'password_vault',
        user = 'postgres',
        password = '1',
        port = 5432
        )