from beanie import init_beanie 
from motor.motor_asyncio import AsyncIOMotorClient
from models.playlists import Playlists
from models.song import Song
from models.users import Users

async def init_db():
    client = AsyncIOMotorClient(
        'DATABASE URI HERE'
    )
    await init_beanie(database=client.jukebox, document_models=[Playlists, Song, Users])