from beanie import Document
from models.song import Song
from models.playlists import Playlists
from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List

class Users(Document):
    name: str
    email: str
    password: str
    registration_date: datetime = datetime.now()
    user_id: str
    songs: List[Song] | None
    playlist: List[Playlists] | None



# class UpdateUser(BaseModel):
#     name: Optional[str]
#     email: Optional[str]
#     registration_date: Optional[datetime]



