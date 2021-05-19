from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAx0CQ8QTWQACCD9gpSGtPso-JueMmC6tCptx2H6VjAACngEAAmpqaFeIQbV46r_aFh8E")
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\nI can play music in your group's voice chat
Maintained by @itsMeLegend ❤
Music Assistant - @camilaowner
\nTo add in your group contact us at @camila_Support
\nHit /help list of available commands.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                      "✨CamilaAssistant", url="https://t.me/camilaowner",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Help Group", url="https://t.me/camila_suppport"
                    ),
                    InlineKeyboardButton(
                        "stickers💖", url="https://t.me/stickersbag"
                    ),
                    InlineKeyboardButton(
                        "✨GitHub✨", url="http://www.github.com/War-Legend"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/camillaMusicbot?startgroup=true"
                    ) 
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support Group  ", url="https://t.me/camila_suppport"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\n/play <song name> - play song you requested
/dplay <song name> - play song you requested via deezer
/splay <song name> - play song you requested via jio saavn
/playlist - Show now playing list
/current - Show now playing
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/saavn <song name> - download songs you want quickly via saavn
/video <song name> - download videos you want quickly
\n*Admins only*
/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/admincache - Refresh admin list
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Need Help❓", url="https://t.me/camila_Support"
                    )
                ]
            ]
        )
    )    
