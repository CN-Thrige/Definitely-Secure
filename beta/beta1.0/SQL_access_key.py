from psycopg2 import *


def get_conn(): #accesing the sql-server
    return connect(
        host = 'localhost',
        dbname = 'main_database',
        user = 'postgres',
        password = '1',
        port = 5432
        )