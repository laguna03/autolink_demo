import app.services.postgre_connector as postgre_connector

conn = postgre_connector.connect_to_database()


conn = postgre_connector.connect_to_database()
cur = conn.cursor()
query = """
CREATE TABLE Users (
    id UUID PRIMARY KEY,
    updated_at DATETIME,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(20),
    date_of_birth DATE,
    employee_num VARCHAR(20),
    user_type ENUM('guest', 'admin')
);
"""
cur.execute(query)
conn.commit()
cur.close()