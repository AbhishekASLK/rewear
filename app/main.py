from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from app.core.config.config import settings
from app.core.utils.static_mounts import mount_static_dirs
from app.modules.landing.router import router as landing_router
from app.modules.auth.router import router as login_router

def get_app() -> FastAPI:
    
    app = FastAPI( **settings.fastapi_kwargs)

    mount_static_dirs(app)

    app.add_middleware(SessionMiddleware, secret_key="rewear")

    app.include_router(landing_router, prefix="/landing", tags=["landing"])
    app.include_router(login_router, prefix="/auth", tags=["auth"])

    return app

app = get_app()
