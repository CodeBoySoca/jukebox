from fastapi import APIRouter, HTTPException, status, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from send_email import JukeBoxEmail
from models.users import Users
from auth.login import Login
from db.redis import Passcode
import secrets
import string
from passlib.hash import pbkdf2_sha256
import datetime

login_router = APIRouter()
templates = Jinja2Templates(directory='templates/')

@login_router.get('/register')
async def register(request: Request):
    return templates.TemplateResponse('registration.html', {'request' : request})
 
@login_router.post('/register')
async def register(request: Request, name: str = Form(), email: str = Form(), password: str = Form()):
    ''' Add user to the db and send passcode and redirect to /passcode'''
    user_result = await Users.find_one(Users.email == email)
    jukebox_email = JukeBoxEmail()
    generated_passcode = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(10))
    passcode = Passcode(passcode=generated_passcode, email=email)
    user_id = secrets.token_hex(9)
    hashed_password = pbkdf2_sha256.hash(password)
    
    #If no user with email create an account
    if user_result is None:
        user = Users(
            name = name,
            email = email,
            password = hashed_password,
            user_id = user_id
        )
        await user.save()
        passcode.save()
        passcode.expire(900)

        jukebox_email.message(
                'Jukebox Registration - Passcode', 
                email,
                templates.get_template("email.html").render({
                    'name' : name, 
                    'passcode' : generated_passcode
                })
            )
        return RedirectResponse(url='passcode', status_code=status.HTTP_302_FOUND)
    #if user has account check their password
    else:
        if _ := pbkdf2_sha256.verify(password, user_result.password):
            passcode.save()
            passcode.expire(900)
            jukebox_email.message(
                'Jukebox Registration - Passcode', 
                email,
                templates.get_template("email.html").render({
                    'name' : name, 
                    'passcode' : generated_passcode
                })
            )
            return RedirectResponse(url='passcode', status_code=status.HTTP_302_FOUND)
        else:
            #Password is incorrect
            return RedirectResponse(url='register', status_code=status.HTTP_302_FOUND)


@login_router.get('/passcode')
async def passcode(request: Request):
    ''' Check for user in the db and send passcode and redirect to /passcode'''
    return templates.TemplateResponse('passcode.html', {'request' : request})


@login_router.post('/passcode')
async def passcode(request: Request, passcode: str = Form()):
    ''' if the passcode is correct send to create a playlist '''
    ''' Check for user in the db and send passcode and redirect to /passcode'''
    if passcode := Passcode.find(Passcode.passcode == passcode).all():
        return RedirectResponse(url='/playlists', status_code=status.HTTP_302_FOUND)
    return templates.TemplateResponse('passcode.html', {'request' : request})


@login_router.get('/login')
async def login(request: Request):
    ''' Check for user in the db and send passcode and redirect to /passcode'''
    
    return templates.TemplateResponse('passcode.html', {'request' : request})