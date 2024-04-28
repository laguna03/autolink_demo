# pylint: disable=E0611
from pydantic import BaseModel


class ExceptionModel(BaseModel):
    detail: str
