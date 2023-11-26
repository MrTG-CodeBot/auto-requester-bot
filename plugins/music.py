import os
import logging
from pyrogram import Client, filters, enums
import requests
from info import GROUP_CHAT_ID

logging.basicConfig(level=logging.INFO)

@Client.on_message(filters.text & filters.group)
async def song(client, message):
    # Check if the message is from the required group
    if message.chat.id == GROUP_CHAT_ID:
        query = message.text

        # Send a request to the Deezer API with the search query
        response = requests.get(f"https://api.deezer.com/search?q={query}")

        # Check if the request was successful
        if response.status_code == 200:
            # Convert the response to JSON format
            result = response.json()

            # Check if there are any search results
            if "data" in result and result["data"]:
                # Get the first result (most relevant result)
                song = result["data"][0]

                # Get the song details
                artist = song["artist"]["name"]
                title = song["title"]
                duration = song["duration"]
                preview_url = song["preview"]

                # Send a message to the user with the song details and a download link
                message_text = f"hey {message.from_user.first_name},\nyour request is {query}\n Artist: {artist}\nTitle: {title}\nDuration: {duration} seconds\nPreview: {preview_url}"
                await client.send_message(message.chat.id, message_text)

                # Send a chat action to indicate that the bot is uploading an audio file
                await client.send_chat_action(message.chat.id, "upload_audio")

                # Send the audio file to the user
                await client.send_audio(message.chat.id, audio=preview_url, title=title, performer=artist)
            else:
                await client.send_message(message.chat.id, "No results found.")
        else:
            await client.send_message(message.chat.id, "Error accessing Deezer API.")
