#!/usr/bin/env python3
import psycopg2
from psycopg2 import sql
from passlib.context import CryptContext
from typing import Optional
from app.services.postgre_connector import connect_to_database, close_connection, create_cursor

# Datos de conexión a la base de datos

# Contexto de hash de contraseña
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Función para obtener el hash de una contraseña
def get_password_hash(password):
    return pwd_context.hash(password)

# Función para verificar una contraseña
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# Función para inicializar la base de datos (crear tabla)
def init_db():
    conn = connect_to_database()
    cur = create_cursor(conn)
    if conn is not None and cur is not None:
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) UNIQUE NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            hashed_password VARCHAR(255) NOT NULL,
            role VARCHAR(10) NOT NULL DEFAULT 'user'
        );
        '''
        try:
            cur.execute(create_table_query)
            conn.commit()
        except (Exception, psycopg2.Error) as error:
            print("Error al crear la tabla:", error)
        finally:
            close_connection(conn)

# Función para crear un usuario
def create_user(username, email, password) -> Optional[int]:
    conn = connect_to_database()
    cur = create_cursor(conn)
    if conn is not None and cur is not None:
        hashed_password = get_password_hash(password)
        insert_user_query = sql.SQL('''
        INSERT INTO users (username, email, hashed_password, role)
        VALUES (%s, %s, %s, %s) RETURNING id;
        ''')
        try:
            cur.execute(insert_user_query, (username, email, hashed_password))
            conn.commit()
            user_id = cur.fetchone()[0]
            return user_id
        except (Exception, psycopg2.Error) as error:
            print("Error al crear usuario:", error)
        finally:
            close_connection(conn)

# Función para verificar el login de un usuario
def verify_user(username, password) -> Optional[dict]:
    conn = connect_to_database()
    cur = create_cursor(conn)
    if conn is not None and cur is not None:
        select_user_query = sql.SQL('''
        SELECT id, hashed_password, role FROM users WHERE username = %s;
        ''')
        try:
            cur.execute(select_user_query, (username,))
            user = cur.fetchone()
            if user and verify_password(password, user[1]):
                return {"id": user[0], "role": user[2]}
            else:
                return None
        except (Exception, psycopg2.Error) as error:
            print("Error al verificar usuario:", error)
        finally:
            close_connection(conn)

# Inicializar la base de datos (crear tabla)
init_db()
