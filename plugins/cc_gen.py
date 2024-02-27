import asyncio
from pyrogram import Client, filters
import requests

@Client.on_message(filters.command("cc"))
async def google_text(client, message):
    try:
        user_query = message.text.split()[1:]
        if not user_query:
          await message.reply_text("Enter a four digit of bin to create the cc") 
          return
        response = requests.get(f"https://api.safone.dev/ccgen?bins={user_query}&limit=1")
        if response.status_code == 200:
            data = response.json()
            bin_data = data['results'][0]
            card = bin_data['cards']
            await client.send_message(message.chat.id, card)

    except Exception as e:
       await message.reply_text(f"An error occurred: {e}")
