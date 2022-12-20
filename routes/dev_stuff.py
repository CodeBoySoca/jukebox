from fastapi import APIRouter, HTTPException, status, Request
from fastapi.templating import Jinja2Templates


api_docs_router = APIRouter()
templates = Jinja2Templates(directory='templates/')


@api_docs_router.get('/dev-stuff')
async def dev_api(request: Request):
    return templates.TemplateResponse('docs.html', {'request': request})

