#!/usr/bin/env python3
# Import the functions from the database_connection.py file
from postgre_connector import connect_to_database, create_cursor, close_connection

# Example function to perform database operations
def fetch_data_from_db():
    # Connect to the database
    connection = connect_to_database()
    if connection:
        try:
            print("Successfully connected to the database.")
            # Create a cursor
            cursor = create_cursor(connection)
            if cursor:
                print("Cursor created successfully.")
                # Execute a query
                cursor.execute("SELECT * FROM your_table")
                print("Query executed successfully.")
                # Fetch data
                data = cursor.fetchall()
                print("Fetched data:", data)
        finally:
            # Close the cursor and connection
            close_connection(connection)
            print("Connection closed successfully.")

# Call the function
fetch_data_from_db()
