from pyrogram import Client, filters, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton                              
from pyrogram.types import CallbackQuery
from plugins.utils.http import get, SOURCE
import asyncio


@Client.on_callback_query()
async def callback(bot, msg):
   data = msg.data
   if data == "help":
       await msg.message.edit(       
           text="""CLICK THE BELOW BUTTONS TO KNOW MY COMMANDS.""",       
           reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("LOGO MAKER", callback_data="logo"),
                  InlineKeyboardButton("PHOTO EDIT", callback_data="editor")
                  ],[
                  InlineKeyboardButton("CARBON", callback_data="carbon"),
                  InlineKeyboardButton("CHANNEL ID", callback_data="ids")
                  ],[
                  InlineKeyboardButton("TELEGRAPH", callback_data="tgraph"),
                  InlineKeyboardButton("FUN GAMES", callback_data="fun")
                  ],[
                  InlineKeyboardButton("PASTE CODE", callback_data="paste"),
                  InlineKeyboardButton("STICKER TOOLS", callback_data="stcker")
                  ],[
                  InlineKeyboardButton("β€οΈβπ©Ή ABOUT", callback_data="about"),
                  InlineKeyboardButton("β€οΈβπ©Ή DEVS", callback_data="devs")
                  ],[
                  InlineKeyboardButton("β©οΈ ππππ", callback_data="start")
                  ]]
                  )
           )
   elif data == "about":
         await msg.message.edit(
             text=f""" 
ββββββ° πΌππ»ππΈ π±πΎπ β±ββ
ββ­ββββββββββββββββ£
ββ£βͺΌπ€α΄Κ Ι΄α΄α΄α΄ : {bot.mention}
ββ£βͺΌπ¦α΄α΄α΄  1 : <a href=https://t.me/about_jeol>α΄α΄α΄Κ</a>
ββ£βͺΌπ¨βπ»α΄α΄α΄  2 : <a href=https://t.me/mr_MKN>α΄Κ.α΄α΄Ι΄ α΄Ι’</a>
ββ£βͺΌβ£οΈsα΄α΄Κα΄α΄ α΄α΄α΄ : <a href=https://github.com/Jeolpaul/TG-MULTI-BOT>α΄Ι’-α΄α΄Κα΄Ιͺ-Κα΄α΄</a>
ββ£βͺΌπ‘Κα΄sα΄α΄α΄ α΄Ι΄ : <a href=https://dashboard.heroku.com>Κα΄Κα΄α΄α΄</a>
ββ£βͺΌπ£οΈΚα΄Ι΄Ι’α΄α΄Ι’α΄ : <a href=https://www.python.org>α΄Κα΄Κα΄Ι΄3</a>
ββ£βͺΌπΚΙͺΚΚα΄ΚΚ : <a href=https://github.com/pyrogram>α΄ΚΚα΄Ι’Κα΄α΄</a> 
ββ£βͺΌποΈα΄ α΄ΚsΙͺα΄Ι΄ : Pyrogram v{__version__}  
ββ°ββββββββββββββββ£
ββββββββββββββββββββ """,
              disable_web_page_preview = True,
              reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("β©οΈ ππππ", callback_data="start"),
                  InlineKeyboardButton("π πππππ", callback_data="close")
                  ]]
                  )
         )        
   elif data == "start":
         await msg.message.edit(
             text=f"Hello {msg.from_user.mention}ππ»\nI'am A Multi Featured Bot With Many Variety Features.\neg:- Telegarph, Channel ID, User ID, Fun, Group Id, Sticker id, kang, and othersetc...\nYou can see My commands by below button...",          
             reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("β¨οΈ Support", url="https://t.me/BETA_SUPPORT"),
                 InlineKeyboardButton("π’ Updates", url="https://t.me/Beta_BoTZ")
                 ],[            
                 InlineKeyboardButton("βΉοΈ Help", callback_data="help"),
                 InlineKeyboardButton("π€ πππππ", callback_data="about")
                  ]]
                  )
         )
   elif data == "devs":
         users = await get("https://api.github.com/repos/jeolpaul/TG-MULTI-BOT/contributors")
         list_of_users = ""
         count = 1
         for user in users:
             list_of_users += (f"**{count}.** [{user['login']}]({user['html_url']})\n")       
             count += 1 
         await msg.message.edit(
             text=SOURCE.format(dev=list_of_users),
             reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("π¨βπ» ππππ 1", user_id=5172114510),
                  InlineKeyboardButton("π¨βπ» ππππ 2", user_id=5652656279)
                  ],[
                  InlineKeyboardButton("β£οΈ ππππππ ππππ β£οΈ", url="https://github.com/Jeolpaul/TG-MULTI-BOT"),
                  ],[
                  InlineKeyboardButton("β©οΈ ππππ", callback_data="start"),
                  InlineKeyboardButton("π πππππ", callback_data="close")
                  ]]
                  )
             )
   elif data == "fun":
         await msg.message.edit(
             text=f"""<b><u>JUST TEST THIS COMMANDS π</u></b>

β /runs         
β /ikka      
β /dice     
β /arrow    
β /goal    
β /luck    
β /throw     
β /bowling  
β /tenpins    
""",      
             reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("β©οΈ ππππ", callback_data="help"),
                 InlineKeyboardButton("π πππππ", callback_data="close")
                 ]]
                 )
             )
   elif data == "tgraph":
         await msg.message.edit(
             text="""β«οΈHELP: TelegraphβͺοΈ

Do as you wish with graph.org module!

USAGE:
β /telegraph - reply to below 5Mb media to get telegraph linkπ―""",
                 reply_markup=InlineKeyboardMarkup( [[  
                     InlineKeyboardButton("β©οΈ ππππ", callback_data="help"),
                     InlineKeyboardButton("π πππππ", callback_data="close")
                     ]]
                     )
             )
   elif data == "logo":
         await msg.message.edit(
             text="""To Make Logo - /logo Your Name
To Make Square Logo -  /logosq Your Name

β»οΈ Example:
/logo BETAs
/logosq MKN""",
                 reply_markup=InlineKeyboardMarkup( [[  
                     InlineKeyboardButton("β©οΈ ππππ", callback_data="help"),
                     InlineKeyboardButton("π πππππ", callback_data="close")
                     ]]
                     )
             )
   elif data == "editor":
         await msg.message.edit(
             text="""β€ πππ₯π©: Iα΄α΄Ι’α΄

ππππ πππππππ πππππ π’ππ ππ ππππ πππππ ππππ’ ππππππ’

β€ ππ¨π¦π¦ππ§ππ¬ ππ§π ππ¬ππ π:
βͺ π©πππ ππΎππ½ ππΎ πΊ πππΊππΎ ππ πΎπ½ππ β¨""",
                 reply_markup=InlineKeyboardMarkup( [[  
                     InlineKeyboardButton("β©οΈ ππππ", callback_data="help"),
                     InlineKeyboardButton("π πππππ", callback_data="close")
                     ]]
                     )
             )
   elif data == "paste":
         await msg.message.edit(
             text="""Help: Paste

Paste some texts or documents on a website!

Commands and Usage:
β’ /paste - Reply To A Message With /paste""",
                 reply_markup=InlineKeyboardMarkup( [[  
                     InlineKeyboardButton("β©οΈ ππππ", callback_data="help"),
                     InlineKeyboardButton("π πππππ", callback_data="close")
                     ]]
                     )
             )
   elif data == "stcker":
         await msg.message.edit(
             text="""β’ πππππ
Convert sticker to photo & create sticker pake & find sticker id.....

β­ ππ€π¬ ππ€ ππ¨π

β /get_sticker - Replay to Any sticker to convert to photo 
β /kang - Reply To Sticker or PNG file to pake sticker 
β /stickerid - Reply To Any Sticker to get id""",
                 reply_markup=InlineKeyboardMarkup( [[  
                     InlineKeyboardButton("β©οΈ ππππ", callback_data="help"),
                     InlineKeyboardButton("π πππππ", callback_data="close")
                     ]]
                     )
             )
   elif data == "ids":
         await msg.message.edit(
             text="""β /id - your tg id & info π
β /stickerid - Reply To Any Sticker to get sticker id
β send channel last message with forward tag to get the channel id π―""",
                 reply_markup=InlineKeyboardMarkup( [[  
                     InlineKeyboardButton("β©οΈ ππππ", callback_data="help"),
                     InlineKeyboardButton("π πππππ", callback_data="close")
                     ]]
                     )
             )
   elif data == "paste":
         await msg.message.edit(
             text="""Help: Paste

Paste some texts or documents on a website!

Commands and Usage:
β’ /paste - Reply To A Message With /paste""",
                 reply_markup=InlineKeyboardMarkup( [[  
                     InlineKeyboardButton("β©οΈ ππππ", callback_data="help"),
                     InlineKeyboardButton("π πππππ", callback_data="close")
                     ]]
                     )
             )
   elif data == "carbon":
         await msg.message.edit(
             text="""βΎοΈππππ£ ππ’π₯ πππ₯ππ’π‘β½οΈ

β /carbon - use this command""",
                 reply_markup=InlineKeyboardMarkup( [[  
                     InlineKeyboardButton("β©οΈ ππππ", callback_data="help"),
                     InlineKeyboardButton("π πππππ", callback_data="close")
                     ]]
                     )
             )
   elif data == "close":
        await msg.message.delete()
        try:
            await msg.message.reply_to_message.delete()
        except:
            pass



















