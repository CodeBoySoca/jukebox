from beanie import init_beanie 
from motor.motor_asyncio import AsyncIOMotorClient
from models.playlists import Playlists
from models.song import Song
from models.users import Users

async def init_db():
    client = AsyncIOMotorClient(
        'mongodb+srv://loverboysoca:fhO9fC7MHQ5DYzgP@jukebox-cluster.eaxenux.mongodb.net/jukebox'
    )
    await init_beanie(database=client.jukebox, document_models=[Playlists, Song, Users])