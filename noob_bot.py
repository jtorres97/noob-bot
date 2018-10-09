import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import config

Client = discord.Client()
client = commands.Bot(command_prefix = " ")

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        # Pong the user back!
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    if message.content.upper().startswith('!SAY'):
        args = message.content.split(" ")
        # Output a formatted sentence
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))

client.run(config.TOKEN)
