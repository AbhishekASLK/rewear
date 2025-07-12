from fastapi.staticfiles import StaticFiles
from app.core.config.config import settings
import os

def mount_static_dirs(app):
    app.mount("/static", StaticFiles(directory=settings.STATIC_DIRS[0]), name="static")
    app.mount("/libs", StaticFiles(directory=settings.APP_DIR / "libs"), name="libs")

    for path in settings.STATIC_DIRS[1:]:
        module_name = path.parts[-2] if path.parts[-1] == "static" else path.parts[-1]
        app.mount(f"/static/{module_name}", StaticFiles(directory=path), name=f"{module_name}-static")
