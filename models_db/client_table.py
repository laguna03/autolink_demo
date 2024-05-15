#!/usr/bin/env python3
""" Create a table in the PostgreSQL database """

import psycopg2


# Establish a connection to the database by creating a connection object
db_connection = psycopg2.connect(
    dbname="autolinkdb",
    user="pedrolaguna",
    password="autolink2024",
    host="localhost",
    port="5432"
)

# Create a cursor object using the cursor() method
cur = db_connection.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS client(
    client_id UUID PRIMARY KEY,
    updated_at TIMESTAMP,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    email VARCHAR,
    phone VARCHAR,
    date_of_birth DATE
);
""")

db_connection.commit()

cur.close()
db_connection.close()
