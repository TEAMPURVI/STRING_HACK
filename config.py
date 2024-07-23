# TEAM PURVI ALL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "27079591"
    API_HASH = "c81ae4c3dc026ea4bf49842a8ce4a5f9"
    #TOKEN = "6521122303:AAGCO3XMjcA0SN5NAi1M0NpmbmMxEtwwYbg"
    TOKEN = os.environ.get("TOKEN", None)
    MONGO_URL = "mongodb+srv://vivek:1234567890@cluster0.c48d8ih.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    START_PIC = "https://telegra.ph/file/c53d9a7df9dbaa5f4db05.jpg"
    SUDOERS = filters.user(["6730956183"])
