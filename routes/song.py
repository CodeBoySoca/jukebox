from fastapi import APIRouter, HTTPException, status, Request, Form, File, UploadFile
from fastapi.templating import Jinja2Templates
from beanie import PydanticObjectId
from models.song import Song
import secrets
import lyricsgenius
import shutil
from tinytag import TinyTag
import os
from PIL import Image
import io
import os.path



song_router = APIRouter()
templates = Jinja2Templates(directory='templates/')
genius = lyricsgenius.Genius('API KEY HERE')


@song_router.get('/add-song')
async def song(request: Request):
    return templates.TemplateResponse('add_song.html', {'request' : request})


@song_router.post('/add-song')
async def song(request: Request, song_upload: UploadFile = File(...)) -> dict:
        with open(f'uploads/songs/{song_upload.filename}', 'wb') as f:
            shutil.copyfileobj(song_upload.file, f)
            tag = TinyTag.get(f'uploads/songs/{song_upload.filename}', image=True)
            album_cover = tag.get_image()
            im = Image.open(io.BytesIO(album_cover))
            im.save(f'uploads/images/{song_upload.filename}.png')
            song = Song(
                    artist = tag.artist,
                    song_title = tag.title,
                    album = tag.album,
                    genre = tag.genre,
                    duration = tag.duration,
                    release_date = tag.year,
                    song_id = secrets.token_urlsafe(16),
                    album_cover = f'uploads/images/{song_upload.filename}.png',
                    likes = 0
            )
            await song.create()    
            genius_search = genius.search_song(tag.title, tag.artist)



        return templates.TemplateResponse('add_song.html', {'request' : request, 'song' : genius_search.lyrics})
     



@song_router.delete('/song/{id}')
async def delete_song(id: PydanticObjectId):
   pass

@song_router.put('/song/{id}')
async def update_song(id: PydanticObjectId):
   pass