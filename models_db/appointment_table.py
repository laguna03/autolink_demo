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

cur.execute("""
ALTER TABLE appointment
ADD FOREIGN KEY (service_id) REFERENCES services(service_id);
""")

db_connection.commit()

cur.close()
db_connection.close()
