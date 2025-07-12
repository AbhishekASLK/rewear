from pathlib import Path
from typing import Any
from fastapi.responses import HTMLResponse
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_DIR: Path = Path(__file__).resolve().parents[2]
    CORE_DIR: Path = APP_DIR / "core"
    MODULES_DIR: Path = APP_DIR / "modules"
    DATA_DIR: Path = APP_DIR / "data"

    ENABLED_MODULES: list[str] = ["landing"]  # Add the modules you want to enable for static files. here

    @property
    def STATIC_DIRS(self) -> list[Path]:
        return [self.APP_DIR / "static"] + [
            self.MODULES_DIR / mod / "static" for mod in self.ENABLED_MODULES
        ]

    @property
    def TEMPLATE_DIRS(self) -> list[Path]:
        base = [
            self.APP_DIR / "core" / "ui" / "templates",
            self.APP_DIR / "core" / "ui",
            self.APP_DIR / "core" / "ui" / "components"
        ]
        module_dirs = []
        for mod in self.ENABLED_MODULES:
            module_base = self.MODULES_DIR / mod / "ui"
            module_dirs.append(module_base / "templates")  # for welcome.html, etc.
            module_dirs.append(module_base)                # for components/
        return base + module_dirs

    @property
    def MODULE_DATA_DIRS(self) -> list[Path]:
        return [self.MODULES_DIR / mod / "data" for mod in self.ENABLED_MODULES]

    @property
    def CORE_DATA_DIR(self) -> Path:
        return self.CORE_DIR / "data"


    FASTAPI_PROPERTIES: dict = {
        "title": "ReWear",
        "description": "Community Clothing Exchange",
        "version": "0.0.1",
        "default_response_class": HTMLResponse,
    }

    DISABLE_DOCS: bool = True

    @property
    def fastapi_kwargs(self) -> dict[str, Any]:
        kwargs = self.FASTAPI_PROPERTIES.copy()
        if self.DISABLE_DOCS:
            kwargs.update(
                {
                    "openapi_url": None,
                    "docs_url": None,
                    "redoc_url": None,
                }
            )
        return kwargs


settings = Settings()
