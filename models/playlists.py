from beanie import Document
from typing import List


class Playlists(Document):
    name: str
    genre: str
    availability: str
    songs: List[str]
    likes: int
    fans: List[str]



