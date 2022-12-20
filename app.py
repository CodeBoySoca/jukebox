from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.index import index_router
from routes.features import features_router 
from routes.dev_stuff import api_docs_router
from routes.playlists import playlists_router
from routes.song import song_router
from db.connection import init_db

import uvicorn


app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')
app.include_router(features_router)
app.include_router(index_router)
app.include_router(api_docs_router)
app.include_router(playlists_router)
app.include_router(song_router)

@app.on_event('startup')
async def start():
    await init_db()

if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=5888, reload=True)