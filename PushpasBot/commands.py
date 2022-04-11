from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant



START_MESSAGE = """ʜᴇy {}, ɪ ᴀᴍ ᴀ ꜱᴩᴇᴄɪᴀʟ ʙᴏᴛ ꜰᴏʀ ᴩyʀᴏɢʀᴀᴍ ᴛᴇꜱᴛ
"""

Force = "updatechannel_forcrime"

@Client.on_message(filters.command("start"))
async def start_msg(bot, msg):
    if Force:
        try:
            user = await bot.get_chat_member(Force, msg.from_user.id)
            if user.status == "kicked out":
                await msg.reply_text("Sᴏʀʀy Bʀᴏ Yᴏᴜ Aʀᴇ Bᴀɴɴᴇᴅ Tᴏ Uꜱᴇ Mᴇ 😂")
                return
        except UserNotParticipant:
          await msg.reply_text(
              text="🔰Bʀᴏ Tʜɪꜱ Iꜱ My Oᴡɴᴇʀꜱ Moᴠɪᴇᴄʜᴀɴɴᴇʟ Pʟᴇᴀꜱᴇ Jᴏɪɴ🔰",
              reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("Mᴏᴠɪᴇ Cʜᴀɴɴᴇʟ 📢", url=f"t.me/{force_channel}")
                 ]]
                 )
          )
          return

await msg.reply_photo(
        photo="https://telegra.ph/file/d6e93a4e09f7993b12fa5.jpg",
        caption=START_MESSAGE.format(msg.from_user.mention),
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("🧛Dᴇᴠ", url="t.me/pushpa_reju")
            
           ]]
           )
    )
