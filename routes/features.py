from fastapi import APIRouter, HTTPException, status, Request
from fastapi.templating import Jinja2Templates


features_router = APIRouter()
templates = Jinja2Templates(directory='templates/')


@features_router.get('/features')
async def features(request: Request):
    return templates.TemplateResponse('features.html', {'request' : request})