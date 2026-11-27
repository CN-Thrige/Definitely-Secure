from SQL_access_key import *

def init_database():
    #this function creates all the tables for the website and accounts if it does not already exist 
    conn = get_conn()
    curr = conn.cursor()

    curr.execute("CREATE EXTENSION IF NOT EXISTS pgcrypto")

    # finger print pseudo
    curr.execute("""
    CREATE TABLE IF NOT EXISTS finger_print_pseudo (
        username VARCHAR(255) UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    # websites
    curr.execute("""
    CREATE TABLE IF NOT EXISTS website (
        website_id SERIAL PRIMARY KEY,
        website_app VARCHAR(255) UNIQUE NOT NULL
    )
    """)

    # website images
    curr.execute("""
    CREATE TABLE IF NOT EXISTS website_images (
        image_id SERIAL PRIMARY KEY,
        website_id INTEGER REFERENCES website(website_id),
        image_data BYTEA NOT NULL
    )
    """)

   # users
    curr.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id SERIAL PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password BYTEA NOT NULL,
        encrypted_key BYTEA NOT NULL,
        website_id INTEGER REFERENCES website(website_id)
    )
    """)


    conn.commit()
    curr.close()
    conn.close()