from fastapi import APIRouter, HTTPException, status, Request
from fastapi.templating import Jinja2Templates

settings_router = APIRouter()
templates = Jinja2Templates(directory='templates/')


@settings_router.get('/settings')
async def settings():
    pass

@settings_router.post('/settings')
async def add_settings():
    pass


