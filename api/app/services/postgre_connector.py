import psycopg2

def connect_to_database():
    try:
        # Establish connection to the PostgreSQL database
        conn = psycopg2.connect(
            dbname="",
            user="",
            password="",
            host="localhost",
            port="5432"
        )
        print("Connection to the database successful")
        return conn
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL:", error)
        return None

def close_connection(conn):
    # Close the connection
    if conn:
        conn.close()
        print("Connection to the database closed")

def create_cursor(conn):
    try:
        # Create a cursor
        cur = conn.cursor()
        print("Cursor created successfully")
        return cur
    except (Exception, psycopg2.Error) as error:
        print("Error while creating cursor:", error)
        return None
