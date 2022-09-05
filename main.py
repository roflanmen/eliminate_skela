from pyrogram import Client
from pyrogram import enums
import asyncio

api_id = 123456789
api_hash = 'abcdefgh12345678' # your telegram app id and hash

cid = -1001515830252 # КН-214 chat id

async def main():
    app = Client("my_account", api_id=api_id, api_hash=api_hash)
    async with app:
        async for message in app.search_messages(cid, limit=100, from_user="skelauwu"): # spam skela, of course; limit - get last 100 messages
            print(message.text) # print to console
            await message.react(emoji="😱") # react with emoji

asyncio.run(main())