from fastapi import APIRouter, HTTPException, status, Request
from fastapi.templating import Jinja2Templates
from beanie import PydanticObjectId
from models.playlists import Playlists
import secrets



playlists_router = APIRouter()
templates = Jinja2Templates(directory='templates/')


@playlists_router.get('/playlists')
async def playlists(request: Request):
   return templates.TemplateResponse('playlists.html', {'request' : request})


@playlists_router.get('/create-playlist')
async def get_playlist(request: Request):
    return templates.TemplateResponse('create_playlist.html', {'request' : request})


@playlists_router.post('/create-playlist', response_description='Create user playlist')
async def create_playlist(playlist: Playlists):
    playlist = await playlist.create()
    return {
        'message' : 'playlist created'
    }

@playlists_router.delete('/delete-playlist')
async def delete_playlist(id: PydanticObjectId):
    pass


@playlists_router.put('/edit-playlist')
async def edit_playlist(id: PydanticObjectId):
    pass