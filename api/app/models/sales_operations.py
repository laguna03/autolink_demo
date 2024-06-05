from fastapi import HTTPException
from app.services import postgre_connector
from .classes.sales_class import Sale


def create_sale(sale_data):
    conn = postgre_connector.connect_to_database()
    try:
        cur = conn.cursor()
        query = "INSERT INTO sale (id, service_id, agent_id, status, updated_at, final_price) VALUES (%s, %s, %s, %s, %s, %s)"
        cur.execute(query, (
            sale_data.id,
            sale_data.service_id,
            sale_data.agent_id,
            sale_data.status,
            sale_data.updated_at,
            sale_data.final_price
        ))
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()

def read_sale(sale_id):
    conn = postgre_connector.connect_to_database()
    try:
        cur = conn.cursor()
        query = "SELECT * FROM sale WHERE id = %s"
        cur.execute(query, (sale_id,))
        sale = cur.fetchone()
        if sale is None:
            raise HTTPException(status_code=404, detail="Sale not found")
        return Sale(
            id=sale[0],
            service_id=sale[1],
            agent_id=sale[2],
            status=sale[3],
            updated_at=sale[4],
            final_price=sale[5]
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()

def update_sale(sale_id, sale_data):
    conn = postgre_connector.connect_to_database()
    try:
        cur = conn.cursor()
        query = "UPDATE sale SET service_id = %s, agent_id = %s, status = %s, updated_at = %s, final_price = %s WHERE id = %s"
        cur.execute(query, (
            sale_data.service_id,
            sale_data.agent_id,
            sale_data.status,
            sale_data.updated_at,
            sale_data.final_price,
            sale_id
        ))
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()

def delete_sale(sale_id):
    conn = postgre_connector.connect_to_database()
    try:
        cur = conn.cursor()
        query = "DELETE FROM sale WHERE id = %s"
        cur.execute(query, (sale_id,))
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()
