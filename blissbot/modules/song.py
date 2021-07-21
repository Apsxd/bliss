from pyrogram import Client, filters
import asyncio
import os
from pytube import YouTube
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from youtubesearchpython import VideosSearch


@Client.on_message(filters.command('music') & ~filters.channel)
def song(client, message):


    user_id = message.from_user.id 
    user_name = message.from_user.first_name 
    rpk = "["+user_name+"](tg://user?id="+str(user_id)+")"

    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply('🔎 Fɪɴᴅɪɴɢ Tʜᴇ Sᴏɴɢ...')
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        #print(results)
        title = results[0]["title"][:40]       
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)

    except Exception as e:
        m.edit(
            "❌ Fᴏᴜɴᴅ Nᴏᴛʜɪɴɢ.\n\nTʀʏ Aɴᴏᴛʜᴇʀ Kᴇʏᴡᴏʀᴋ Oʀ Mᴀʏʙᴇ Sᴘᴇʟʟ Iᴛ Pʀᴏᴘᴇʀʟʏ"
        )
        print(str(e))
        return
    m.edit("Downloading the song ")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = '**🎵 Uploaded by @Missblissrobot**'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(audio_file, caption=rep, thumb=thumb_name, parse_mode='md', title=title, duration=dur)
        m.delete()
    except Exception as e:
        m.edit('❌ Eʀʀᴏʀ')
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
