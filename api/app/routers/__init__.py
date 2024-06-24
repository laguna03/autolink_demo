from sys import prefix
from app.routers.agent_crud import router as agent_router
from app.routers.appointment_crud import router as appointment_router
from app.routers.client_crud import router as client_router
from app.routers.service_crud import router as service_router
from app.routers.vehicle_crud import router as vehicle_router
from app.routers.sales_crud import router as sales_router
from app.routers.user_crud import router as user_router
from app.routers.health import router as health_router


def add_routers(app):
    app.include_router(health_router, prefix="/health", tags=["Health"])
    app.include_router(agent_router, prefix="/agent", tags=["Agents"])
    app.include_router(appointment_router,
                       prefix="/appointment", tags=["Appointments"])
    app.include_router(client_router, prefix="/client", tags=["Clients"])
    app.include_router(service_router, prefix="/service", tags=["Services"])
    app.include_router(vehicle_router, prefix="/vehicle", tags=["Vehicles"])
    app.include_router(sales_router, prefix="/sales", tags=["Sales"])
    app.include_router(user_router, prefix="/user", tags=["Users"])
