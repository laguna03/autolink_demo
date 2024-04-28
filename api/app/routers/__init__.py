from sys import prefix


def add_routers(app):
    app.include_router(detect_router, prefix="/detect", tags=["Object detection API"])
