from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from app.core.templating.template_utils import render


router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def landing(request: Request):
    context = {}
    return render("landing.html", request, context)
