from fastapi.applications import FastAPI
from API.routes import root
from API.routes.User import user_controll

def register_routers(app: FastAPI) -> FastAPI:
    app.include_router(root.router)
    app.include_router(user_controll.router, prefix='/api/v1.0/users')
    return app