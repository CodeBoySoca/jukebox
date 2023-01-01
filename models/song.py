from beanie import Document
from datetime import datetime


class Song(Document):
    artist: str
    song_title: str
    duration: str 
    album: str
    release_date: str
    likes: int
    genre: str
    song_id: str
    album_cover: str | None
    lyrics: str | None

    def format_lyrics(lyrics):
        ''' This method formats the lyrics received from the LyricsGenius API, 
            creating whitespace and stripping unnecessary characters '''
        pass
        

    
