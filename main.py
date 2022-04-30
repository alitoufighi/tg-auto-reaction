from pyrogram import filters
from client import app
from dotenv import load_dotenv
import os

load_dotenv()

victim_ids = os.getenv('VICTIM_USER_IDS')
group_ids = os.getenv('VICTIM_GROUP_IDS')

if not (victim_ids or group_ids):
    raise Exception('You have to pass both VICTIM_USER_IDS and VICTIM_GROUP_IDS env variables')


@app.on_message(
    filters.chat(list(map(int, group_ids.split(',')))) &
    filters.user(list(map(int, victim_ids.split(','))))
)
async def react(_, message):
    await message.react(emoji='💩')


app.run()
