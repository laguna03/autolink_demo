""" Create a table in the PostgreSQL database """

import psycopg2


# Establish a connection to the database by creating a connection object
db_connection = psycopg2.connect(
    dbname="",
    user="",
    password="",
    host="localhost",
    port="5432"
)

# Create a cursor object using the cursor() method
cur = db_connection.cursor()


#define sql command to create a table
cur.execute("""
ALTER TABLE vehicle
ADD FOREIGN KEY (client_id) REFERENCES client(client_id);
""")

db_connection.commit()

cur.close()
db_connection.close()
