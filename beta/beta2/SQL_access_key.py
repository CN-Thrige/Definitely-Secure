from psycopg2 import * #wildcard = import everything 


def get_conn(): #accesing the sql-server / get connection to the server
    return connect(
        host = 'localhost',
        dbname = 'main_database',
        user = 'postgres',
        password = '1', #should probaly be encrypted...
        port = 5432
        )