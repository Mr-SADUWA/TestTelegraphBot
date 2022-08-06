import os

from pyrogram import filters,Client
from telegraph import upload_file
from config import Config

app = Client(
   "Telegraph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.BOT_TOKEN,
)

@app.on_message(filters.command("start"))
async def telegraph(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply("Hey..!I'm Telegraph Uploader😁\n\n☘️ DᕮᐯᕮᒪOᑭᕮR : @NidushaAmarasinghe \n Support : @STM_Developers")
        return


@app.on_message(filters.command("Upload"))
async def telegraph(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply("Reply to a supported media file")
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_name.endswith(".mp4")
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".mp4"),
            )
            and replied.document.file_size <= 5242880
        )
    ):
        await message.reply("Not supported!")
        return
    download_location = await client.download_media(
        message=message.reply_to_message,
        file_name="root/downloads/",
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply(message, text=document)
    else:
        await message.reply(
            f"**Uploaded To Telegraph!\n\n👉 https://telegra.ph{response[0]}**",
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)
        
print("Bot Start ✅")
app.run()
