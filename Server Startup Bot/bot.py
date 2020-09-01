# bot.py
import subprocess
import os
import random
import discord
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()
@client.event
async def on_ready():
    print(f'{client.user} is ready to start servers up.')
@client.event
async def on_message(message):
    #if message.channel.id == "740277052074360903":
        #print("1")
    if message.content == "start":
        print("2")
        await message.channel.send('Server Starting...')
        subprocess.call([r"C:\Users\phoni\Desktop\Magma Server\run.bat"],shell=True)
    else:
        print("9")
client.run(TOKEN)
