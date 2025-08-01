from pydantic import BaseModel
from typing import Optional
from uuid import UUID

 

class SubBase(BaseModel):
    link: str

class SubCreate(SubBase):
    pass



class SubUpdate(BaseModel):
    link: str

