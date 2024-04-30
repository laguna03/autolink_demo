"""
Main module of the application file
"""

import os
from datetime import datetime
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import add_routers
from app.routers.dependencies import application_settings
from app.settings.logger import init_logger

init_logger()

settings = application_settings()

app = FastAPI(
    title="AutoLink",
    description=f"<b>Environment:</b> {settings.environment_name}<br><b>Version:</b> {settings.app_version}<br><b>Release Date:</b> {settings.app_release_date}<br><b>Starting Date:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
    version=settings.app_version,
)

if settings.environment_name == "local":
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

add_routers(app)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("API_PORT", "8083")))
