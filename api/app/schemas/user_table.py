#!/usr/bin/env python3
import psycopg2
from psycopg2 import sql
from passlib.context import CryptContext
from services import postgre_connector

conn = postgre_connector.connect_to_database()

# Initialize password context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function to get password hash
def get_password_hash(password):
    return pwd_context.hash(password)

# Function to verify password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Function to initialize the database (create table)
def init_db():
    conn = postgre_connector.connect_to_database()
    cur = postgre_connector.create_cursor(conn)
    if conn is not None and cur is not None:
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) UNIQUE NOT NULL,
            hashed_password VARCHAR(255) NOT NULL,
            role VARCHAR(10) NOT NULL DEFAULT 'user'
        );
        '''
        try:
            cur.execute(create_table_query)
            conn.commit()
            print("Table created successfully")
        except (Exception, psycopg2.Error) as error:
            print("Error creating table:", error)
        finally:
            postgre_connector.close_connection(conn)

# Function to create a user
def create_user(username, password, role='user'):
    conn = postgre_connector.connect_to_database()
    cur = postgre_connector.create_cursor(conn)
    if conn is not None and cur is not None:
        hashed_password = get_password_hash(password)
        insert_user_query = sql.SQL('''
        INSERT INTO users (username, hashed_password, role)
        VALUES (%s, %s, %s) RETURNING id;
        ''')
        try:
            cur.execute(insert_user_query, (username, hashed_password, role))
            conn.commit()
            user_id = cur.fetchone()[0]
            print(f"User {username} created successfully with id {user_id}")
            return user_id
        except (Exception, psycopg2.Error) as error:
            print("Error creating user:", error)
        finally:
            postgre_connector.close_connection(conn)

# Function to verify user login
def verify_user(username, password):
    conn = postgre_connector.connect_to_database()
    cur = postgre_connector.create_cursor(conn)
    if conn is not None and cur is not None:
        select_user_query = sql.SQL('''
        SELECT id, hashed_password, role FROM users WHERE username = %s;
        ''')
        try:
            cur.execute(select_user_query, (username,))
            user = cur.fetchone()
            if user and verify_password(password, user[1]):
                print("Login successful")
                return {"id": user[0], "role": user[2]}
            else:
                print("Invalid username or password")
                return None
        except (Exception, psycopg2.Error) as error:
            print("Error verifying user:", error)
        finally:
            postgre_connector.close_connection(conn)

# Initialize the database (create table)
init_db()

# Example usage: create a user
# create_user('admin', 'adminpassword', 'admin')

# Example usage: verify user login
# user_info = verify_user('admin', 'adminpassword')
# print(user_info)
