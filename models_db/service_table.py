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
cur.execute( """
CREATE TABLE services (
    service_id SERIAL PRIMARY KEY,
    service_name VARCHAR(50),
    service_description varchar(155) NOT NULL,
    service_duration INTEGER,
    service_price INTEGER
);
""")

db_connection.commit()

cur.close()
db_connection.close()
