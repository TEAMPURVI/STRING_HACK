import os
import asyncio
import logging
from config import Config
from pyrogram import Client
from rich.console import Console
from rich.table import Table
from RAUSHAN.Helpers.data import LOG_TEXT
from pyromod import listen 

#getting variables
API_ID = Config.API_ID
API_HASH = Config.API_HASH
TOKEN = Config.TOKEN
START_PIC = Config.START_PIC



if not START_PIC:
    START_PIC = "https://telegra.ph/file/c53d9a7df9dbaa5f4db05.jpg"

#rich
LOG = Console()

#logger
logging.basicConfig(level=logging.INFO)

#client
app = Client(
    "SupremeStark",
    api_id = API_ID,
    api_hash = API_HASH,
    bot_token = TOKEN )
    


async def RAUSHAN():
    os.system("clear")
    header = Table(show_header=True, header_style="bold green")
    header.add_column(LOG_TEXT)
    LOG.print(header)
    LOG.print(f"[bold cyan]𝐓𝐄𝐀𝐌 𝐏𝐔𝐑𝐕𝐈 𝐁𝐎𝐓𝐒")
    LOG.print("[bold yellow]𝐘𝐨𝐮𝐫 𝐁𝐨𝐭 𝐒𝐭𝐚𝐫𝐭.............")
    await app.start()    
    


loop = asyncio.get_event_loop()
loop.run_until_complete(RAUSHAN())    
