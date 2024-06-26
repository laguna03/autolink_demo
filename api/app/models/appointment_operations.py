from fastapi import HTTPException
from app.services import postgre_connector
from .classes.appointment_class import AppointmentData


def create_appointment(appointment_data: AppointmentData):
    conn = postgre_connector.connect_to_database()
    try:
        cur = conn.cursor()
        query = "INSERT INTO autolink.appointments (appt_id, agent_id, client_id, service_id, vehicle_id, created_at, status, appt_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cur.execute(query, (
            appointment_data.appt_id,
            str(appointment_data.agent_id),
            str(appointment_data.client_id),
            appointment_data.service_id,
            appointment_data.vehicle_id,
            appointment_data.created_at,
            appointment_data.status,
            appointment_data.appt_time
        ))
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()


def read_appointment(appointment_id: int):
    conn = postgre_connector.connect_to_database()
    try:
        cur = conn.cursor()
        query = "SELECT * FROM appointment WHERE id = %s"
        cur.execute(query, (appointment_id,))
        appointment = cur.fetchone()
        if appointment is None:
            raise HTTPException(status_code=404, detail="Appointment not found")
        return AppointmentData(
            id=appointment[0],
            agent_id=appointment[1],
            sale_id=appointment[2],
            client_id=appointment[3],
            service_id=appointment[4],
            vehicle_id=appointment[5],
            created_at=appointment[6],
            status=appointment[7],
            appt_time=appointment[8]
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()


def update_appointment(appointment_id: int, appointment_data: AppointmentData):
    conn = postgre_connector.connect_to_database()
    try:
        cur = conn.cursor()
        query = "UPDATE appointment SET agent_id = %s, sale_id = %s, client_id = %s, service_id = %s, vehicle_id = %s, created_at = %s, status = %s, appt_time = %s WHERE id = %s"
        cur.execute(query, (
            str(appointment_data.agent_id),
            appointment_data.sale_id,
            str(appointment_data.client_id),
            appointment_data.service_id,
            appointment_data.vehicle_id,
            appointment_data.created_at,
            appointment_data.status,
            appointment_data.appt_time,
            appointment_id
        ))
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()


def delete_appointment(appointment_id: int):
    conn = postgre_connector.connect_to_database()
    try:
        cur = conn.cursor()
        query = "DELETE FROM appointment WHERE id = %s"
        cur.execute(query, (appointment_id,))
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()
