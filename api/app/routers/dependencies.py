"""
Dependencies.
"""
from typing import Iterator
from fastapi import Depends
from sqlalchemy.orm import Session
from app.settings.application import ApplicationSettings


def application_settings() -> ApplicationSettings:
    """
    Dependency to return the settings for the App.
    """
    return ApplicationSettings()
