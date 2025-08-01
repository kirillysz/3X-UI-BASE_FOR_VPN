from pydantic import BaseModel

class SubBase(BaseModel):
    link: str

class SubCreate(SubBase):
    pass

class SubUpdate(BaseModel):
    link: str