from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
import os
from os import environ

EVAL_ID = int(os.environ.get("EVAL_ID", "-1002002636126"))

@Client.on_message(filters.text & filters.chat(int(EVAL_ID)))
async def echo(client: Client, message: Message):
    try:
        msg = message.text
        msg = msg.lower()
        if msg == "hi":
            await message.reply_text(f"Hello {message.from_user.mention}")
        elif msg == "bye":
            await message.reply_text(f"Bye {message.from_user.mention}")
        elif msg == "how are you":
            await message.reply_text("I am fine, and you?")
        elif msg == "i am fine":
            await message.reply_text("Do u use my features")
        elif msg == "yes":
            await message.reply_text("Thanks for using my feature")
        elif msg == "no":
            await message.reply_text("use it click /help")
        elif msg == "ok i will try":
            await message.reply_text("mm")
        elif msg == "who is your owner":
            await message.reply_text(f"<a href='tg://user?id=1342641151><b> <^ ~ ^> ᴍʀ.ʙᴏᴛ ᵀᴳ </> </b></a>")
        elif msg == "who is ur owner":
            await message.reply_text(f"<a href='tg://user?id=1342641151><b> <^ ~ ^> ᴍʀ.ʙᴏᴛ ᵀᴳ </> </b></a>") 
        elif msg == "which model are you using ?":
            await message.reply_text("<^ ~ ^> ᴍʀ.ʙᴏᴛ ᵀᴳ </> is made me, i think you should ask him.")
        elif msg == "which model are you using?":
            await message.reply_text("<^ ~ ^> ᴍʀ.ʙᴏᴛ ᵀᴳ </> is made me, i think you should ask him.")
        elif msg == "which ai are you using ?":
            await message.reply_text("<^ ~ ^> ᴍʀ.ʙᴏᴛ ᵀᴳ </> is made me, i think you should ask him.")
        elif msg == "which ai are you using?":
            await message.reply_text("<^ ~ ^> ᴍʀ.ʙᴏᴛ ᵀᴳ </> is made me, i think you should ask him.")    
        elif msg == "which ai model are you using ?":
            await message.reply_text("<^ ~ ^> ᴍʀ.ʙᴏᴛ ᵀᴳ </> is made me, i think you should ask him.")
        elif msg == "which ai model are you using?":
            await message.reply_text("<^ ~ ^> ᴍʀ.ʙᴏᴛ ᵀᴳ </> is made me, i think you should ask him.") 
        elif msg == "what is your name ?":
            await message.reply_text("my name is ᴏʙᴀɴᴀɪ")
        elif msg == "what is your name?":
            await message.reply_text("my name is ᴏʙᴀɴᴀɪ")
        elif msg == "what is ur name ?":
            await message.reply_text("my name is ᴏʙᴀɴᴀɪ")
        elif msg == "what is ur name?":
            await message.reply_text("my name is ᴏʙᴀɴᴀɪ")
        elif msg == "how to deploy a bot":
            await message.reply_text(f"ask him: <a href='tg://user?id=1342641151><b> <^ ~ ^> ᴍʀ.ʙᴏᴛ ᵀᴳ </> </b></a>")
        elif msg == "can u send ur repo":
            await message.reply_text("yup, why not repo:- https://github.com/MrTG-CodeBot/Obanai")
        elif msg == "which server are u using ?":
            await message.reply_text("idk")
        elif msg == "which server are u using?":
            await message.reply_text("idk")     
        elif msg == "which server are u using":
            await message.reply_text("idk")  
        else:
            pass
    except Exception as e:
        await message.reply_text(f"{e}")