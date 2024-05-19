from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton("𝐂𝐡𝐚𝐭 𝐆𝐩𝐓", callback_data="mplus HELP_ChatGPT"),InlineKeyboardButton("𝐆𝐫𝐨𝐮𝐩𝐬", callback_data="mplus HELP_Group"),InlineKeyboardButton("𝐒𝐭𝐢𝐜𝐤𝐞𝐫𝐬", callback_data="mplus HELP_Sticker")],
    [InlineKeyboardButton("𝐓𝐚𝐠 𝐀𝐥𝐥", callback_data="mplus HELP_TagAll"),
    InlineKeyboardButton("𝐈𝐧𝐟𝐨", callback_data="mplus HELP_Info"),InlineKeyboardButton("𝐄𝐱𝐭𝐫𝐚", callback_data="mplus HELP_Extra")],
    [InlineKeyboardButton("𝐈𝐦𝐚𝐠𝐞", callback_data="mplus HELP_Image"),
    InlineKeyboardButton("𝐀𝐜𝐭𝐢𝐨𝐧", callback_data="mplus HELP_Action"),InlineKeyboardButton("𝐒𝐞𝐚𝐫𝐜𝐡", callback_data="mplus HELP_Search")],    
    [InlineKeyboardButton("𝐅𝐨𝐧𝐭", callback_data="mplus HELP_Font"),
    InlineKeyboardButton("𝐆𝐚𝐦𝐞𝐬", callback_data="mplus HELP_Game"),InlineKeyboardButton("𝐓 𝐆𝐫𝐚𝐩𝐡", callback_data="mplus HELP_TG")],
    [InlineKeyboardButton("𝐈𝐦𝐩𝐨𝐒𝐭𝐞𝐫", callback_data="mplus HELP_Imposter"),
    InlineKeyboardButton("𝐓𝐫𝐮𝐭𝐡 𝐃𝐚𝐫𝐞", callback_data="mplus HELP_TD"),InlineKeyboardButton("𝐇𝐚𝐬𝐭𝐚𝐠", callback_data="mplus HELP_HT")], 
    [InlineKeyboardButton("𝐓𝐭𝐬", callback_data="mplus HELP_TTS"),
    InlineKeyboardButton("𝐅𝐮𝐧", callback_data="mplus HELP_Fun"),InlineKeyboardButton("𝐐𝐮𝐨𝐭𝐥𝐲", callback_data="mplus HELP_Q")],          
    [InlineKeyboardButton("<🔘", callback_data=f"settings_back_helper"), 
    InlineKeyboardButton("🔘>", callback_data=f"managebot123 settings_back_helper"),
    ]]
