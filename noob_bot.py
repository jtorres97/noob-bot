import discord
from discord.ext import commands
import asyncio
from datetime import datetime

# Configuration file(s)
import configparser
import sys, traceback

# Load configuration to get around hard coded tokens
config = configparser.ConfigParser()
with open('config.ini') as config_file:
    config.read_file(config_file)

# Set up command prefix and bot description
client = commands.Bot(command_prefix = '.', description = 'Josh\'s first bot.')
client.remove_command('help')
client.launch_time = datetime.utcnow()

# Extentions added by default
startup_extensions = [
    'cogs.basic', 
    'cogs.fun',
    'cogs.util',
    'cogs.user'
    ]

@client.event
async def on_ready():
    # Print some stuff when the bot goes online
    print('------------------------------------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Discord.py Version: ' + str(discord.__version__))
    print('------------------------------------')

# Removes X amount of messages from a discord channel
# .clear
@client.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount) 

@client.command()
async def uptime(ctx):
    delta_uptime = datetime.utcnow() - client.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    await ctx.send(f"{days}d, {hours}h, {minutes}m, {seconds}s")

if __name__ == '__main__':
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            print('Failed to load extension ' + extension, file=sys.stderr)
            traceback.print_exc()    
    
client.run(config.get(section='Configuration', option='connection_token'),
           bot=True, reconnect=True)
