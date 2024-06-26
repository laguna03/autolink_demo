#!/usr/bin/env python3
import psycopg2
<<<<<<< HEAD
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
=======
from app.settings.application import get_settings
from app.settings.logger import get_logger

logger = get_logger()
settings = get_settings()

>>>>>>> main

def connect_to_database():
    try:
        # Establish connection to the PostgreSQL database
        conn = psycopg2.connect(
<<<<<<< HEAD
            dbname="autolinkdb",
            user="manuel",
            password="mitsubishi",
            host="localhost",
            port="5432"
=======
            dbname=settings.postgres_db,
            user=settings.postgres_user,
            password=settings.postgres_password,
            host=settings.postgres_host,
            port=settings.postgres_port
>>>>>>> main
        )
        logger.info("Connection to the database successful")
        return conn
    except (Exception, psycopg2.Error) as error:
        logger.error("Error while connecting to PostgreSQL:", error)
        return None


def close_connection(conn):
    # Close the connection
    if conn:
        conn.close()
        logger.info("Connection to the database closed")


def create_cursor(conn):
    try:
        # Create a cursor
        cur = conn.cursor()
        logger.info("Cursor created successfully")
        return cur
    except (Exception, psycopg2.Error) as error:
        logger.error("Error while creating cursor:", error)
        return None

engine = create_engine("postgresql://manuel:mitsubishi@localhost/autolinkdb")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()