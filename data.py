from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🙄 ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ 🙄", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("❣️ sᴜᴩᴩᴏʀᴛ ❣️", url="https://t.me/DevilsHeavenMF"),
         InlineKeyboardButton("🥀 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🥀", url="https://t.me/anonymous_was_bot"),
        ],
    ]

    START = """
𝙷𝚎𝚢 𝙱𝚊𝚋𝚞 {},

𝚃𝚑𝚒𝚜 𝚒𝚜 {},
𝚂𝚝𝚛𝚒𝚗𝚐 𝚂𝚎𝚜𝚜𝚒𝚘𝚗 𝙶𝚎𝚗𝚎𝚛𝚊𝚝𝚘𝚛 𝙱𝚘𝚝, 𝚆𝚛𝚒𝚝𝚝𝚎𝚗 𝚒𝚗 𝙿𝚢𝚝𝚑𝚘𝚗 𝚆𝚒𝚝𝚑 𝚃𝚑𝚎 𝙷𝚎𝚕𝚙 𝙾𝚏 𝙿𝚢𝚛𝚘𝚐𝚛𝚊𝚖.

[𝙶-𝙽𝚎𝚝𝚠𝚘𝚛𝚔](https://t.me/Groot_Network)
🌱𝙾𝚆𝙽𝙴𝚁 : [𝙸𝚊𝚖 𝙶𝚛𝚘𝚘𝚝](https://t.me/Mynameisgroot) !
    """
