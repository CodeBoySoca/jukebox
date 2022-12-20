from beanie import Document
import uuid
from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class Users(Document):
    name: str
    email: str
    registration_date: datetime = datetime.now()
    user_id: int

class UpdateUser(BaseModel):
    name: Optional[str]
    email: Optional[str]
    registration_date: Optional[datetime]



