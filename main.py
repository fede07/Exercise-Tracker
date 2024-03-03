from dotenv import load_dotenv
from os import getenv

load_dotenv(".env")

APP_ID = getenv("APP_ID")
API_KEY = getenv("API_KEY")

print(APP_ID)
print(API_KEY)