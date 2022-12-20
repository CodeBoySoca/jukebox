from fastapi import APIRouter, HTTPException, status, Request
from fastapi.templating import Jinja2Templates
from typing import List

index_router = APIRouter()
templates = Jinja2Templates(directory='templates/')


@index_router.get('/')
async def index(request: Request):
    return templates.TemplateResponse('index.html', {'request' : request})