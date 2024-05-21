from fastapi import HTTPException
from app.services import postgre_connector
from models.classes.client_class import ClientData

def create_client(client_data):
    conn = postgre_connector.connect_to_database()
    try:
        cur = conn.cursor()
        query = "INSERT INTO clients (id, updated_at, first_name, last_name, email, phone, date_of_birth) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cur.execute(query, (
            str(client_data.id),
            client_data.updated_at,
            client_data.first_name,
            client_data.last_name,
            client_data.email,
            client_data.phone,
            client_data.date_of_birth
        ))
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()


def read_client(client_id=None, first_name=None, last_name=None, email=None, phone=None, date_of_birth=None):
    # Create a list to store conditions for WHERE clause
    conditions = []
    params = []

    # Check each parameter and add condition to the list if not None
    if client_id:
        conditions.append("id = %s")
        params.append(str(client_id))
    if first_name:
        conditions.append("first_name = %s")
        params.append(first_name)
    if last_name:
        conditions.append("last_name = %s")
        params.append(last_name)
    if email:
        conditions.append("email = %s")
        params.append(email)
    if phone:
        conditions.append("phone = %s")
        params.append(phone)
    if date_of_birth:
        conditions.append("date_of_birth = %s")
        params.append(date_of_birth)

    # Join conditions with 'AND' and create the WHERE clause
    where_clause = " AND ".join(conditions)

    # Connect to the database
    conn = postgre_connector.connect_to_database()
    try:
        cur = conn.cursor()
        query = "SELECT * FROM clients"
        if where_clause:
            query += " WHERE " + where_clause
        cur.execute(query, tuple(params))
        clients = cur.fetchall()
        if not clients:
            raise HTTPException(status_code=404, detail="Clients not found")
        return [ClientData(
            id=client[0],
            updated_at=client[1],
            first_name=client[2],
            last_name=client[3],
            email=client[4],
            phone=client[5],
            date_of_birth=client[6]
        ) for client in clients]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()


def update_client(client_id, client_data):
    conn = postgre_connector.connect_to_database()
    try:
        cur = conn.cursor()
        query = "UPDATE clients SET updated_at = %s, first_name = %s, last_name = %s, email = %s, phone = %s, date_of_birth = %s WHERE id = %s"
        cur.execute(query, (
            client_data.updated_at,
            client_data.first_name,
            client_data.last_name,
            client_data.email,
            client_data.phone,
            client_data.date_of_birth,
            str(client_id)
        ))
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()


def delete_client(client_id):
    conn = postgre_connector.connect_to_database()
    try:
        cur = conn.cursor()
        query = "DELETE FROM clients WHERE id = %s"
        cur.execute(query, (str(client_id),))
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()