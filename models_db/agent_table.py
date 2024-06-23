#!/usr/bin/env python3
from sqlalchemy import Column, String, Integer, TIMESTAMP, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
import uuid

Base = declarative_base()

class Agent(Base):
    __tablename__ = "agents"

    agent_ID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    updated_at = Column(TIMESTAMP, server_default=func.now())
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    emp_number = Column(String, nullable=False)