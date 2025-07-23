from dotenv import load_dotenv
from os import getenv

load_dotenv(dotenv_path="app/.env")

class Config:
    DATABASE_URL = getenv("DATABASE_URL")
    
