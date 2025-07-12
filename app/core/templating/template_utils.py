from pathlib import Path
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from jinja2 import ChoiceLoader, FileSystemLoader, Environment

from app.core.config.config import settings
from app.core.i18n.locale import get_translations

# Environment Setup

def create_jinja_environment(template_dirs: list[Path]) -> Environment:
    loaders = [FileSystemLoader(str(p)) for p in template_dirs]
    env = Environment(loader=ChoiceLoader(loaders), autoescape=True)
    env.globals["_"] = lambda s: s  # Default no-op translation
    return env

env = create_jinja_environment(settings.TEMPLATE_DIRS)
templates = Jinja2Templates(env=env)

# i18n Injection

def apply_module_locale(env: Environment, template_path: str, request: Request):
    for base_path in settings.TEMPLATE_DIRS:
        full_path = base_path / template_path
        if full_path.exists() and "modules" in full_path.parts:
            try:
                mod_index = full_path.parts.index("modules")
                module_name = full_path.parts[mod_index + 1]
                locale = request.cookies.get("locale", "en")
                i18n_root = settings.MODULES_DIR / module_name / "i18n"
                env.globals["_"] = get_translations(i18n_root, locale)
            except Exception as e:
                env.globals["_"] = lambda s: s
            break
    else:
        env.globals["_"] = lambda s: s

# Base Template Heuristic

def guess_base_template(template_path: str) -> str | None:
    for base_path in settings.TEMPLATE_DIRS:
        full_path = base_path / template_path
        if full_path.exists() and "modules" in full_path.parts:
            try:
                mod_index = full_path.parts.index("modules")
                module_name = full_path.parts[mod_index + 1]
                return f"{module_name}_base.html"
            except IndexError:
                return None
    return None

# Template Rendering Entry Point

def render(template_path: str, request: Request, context: dict) -> HTMLResponse:
    context["request"] = request

    apply_module_locale(env, template_path, request)

    if request.headers.get("hx-request") == "true":
        return templates.TemplateResponse(template_path, context)

    if template_path.endswith("_base.html"):
        raise ValueError(f"❌ Refusing to inject layout template directly: {template_path}")

    base_template = guess_base_template(template_path)
    if base_template:
        context["content_template"] = template_path
        return templates.TemplateResponse(base_template, context)

    return templates.TemplateResponse(template_path, context)


def render_to_string(template_name: str, request: Request, context: dict) -> str:
    return templates.get_template(template_name).render(context)