from pyrogram import Client
from dotenv import load_dotenv
import os

load_dotenv()

api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')

if not (api_id or api_hash):
    raise Exception('You have to pass both API_ID and API_HASH env variables')

app = Client("auto-reaction", api_id, api_hash)
