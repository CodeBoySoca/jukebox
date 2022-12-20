from fastapi import APIRouter, HTTPException, status, Request
from fastapi.templating import Jinja2Templates


login_router = APIRouter()
templates = Jinja2Templates(directory='templates/')

@login_router.get('/login')
async def login(request: Request):
    return templates.TemplateResponse('login.html', {'request' : request})
   
@login_router.post('/login')
async def login():
    pass

@login_router.get('/confirmation')
async def confirmation():
    pass

@login_router.post('/confirmation')
async def confirmation():
    pass