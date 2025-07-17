from dotenv import load_dotenv
from os import getenv

load_dotenv(dotenv_path=".env")

class Config:
    XUI_HOST = getenv("XUI_HOST")
    XUI_USERNAME = getenv("XUI_USERNAME")
    XUI_PASSWORD = getenv("XUI_PASSWORD")

