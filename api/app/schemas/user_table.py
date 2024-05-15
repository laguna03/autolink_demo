import app.services.postgre_connector as postgre_connector

# connect to database
conn = postgre_connector.connect_to_database()
# create a cursor
cur = conn.cursor()

# create a table
query = """
CREATE TABLE Users (
    id UUID PRIMARY KEY,
    updated_at TIMESTAMP,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(20),
    date_of_birth DATE,
    employee_num VARCHAR(20),
    user_type ENUM('guest', 'admin')
);
"""

# execute the query
cur.execute(query)
# commit the changes
conn.commit()
# close the cursor
cur.close()
# close the connection
conn.close()