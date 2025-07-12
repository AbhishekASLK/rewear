from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from app.core.templating.template_utils import render

router = APIRouter()

@router.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    context = {}
    return render("login.html", request, context)

@router.get("/register", response_class=HTMLResponse)
async def login(request: Request):
    context = {}
    return render("register.html", request, context)
