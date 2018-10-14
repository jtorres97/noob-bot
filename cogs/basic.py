import discord
from discord.ext import commands

import traceback
import random

class BasicCog:
    def __init__(self, bot):
        self.bot = bot

    # Simple ping command
    # Replies back to the command context with the text "Pong!"
    # .ping
    @commands.cooldown(1, 1, commands.BucketType.user)
    @commands.command(name='ping')
    async def ping(self, ctx):
        await ctx.send("Pong!")

    # A simple command which only responds to the owner of the bot
    # .me
    @commands.command(name='me')
    @commands.is_owner()
    async def only_me(self, ctx):
        await ctx.send(f'Hello {ctx.author.mention}. This command can only be used by you!')

    # Is the bot cool?
    # .coolbot
    @commands.command(name='coolbot')
    async def cool_bot(self, ctx):
        await ctx.send('This bot is cool. :)')

    # Gets the avatar of a selected user
    # .getAvatar @user
    @commands.cooldown(1, 1, commands.BucketType.user)
    @commands.command(name='getAvatar')
    async def getAvatar(self, ctx, searchUser):
        result = ""
        for member in ctx.guild.members:
            if member.mention == searchUser:
                result = member.avatar_url
        await ctx.send(f'{searchUser}\'s avatar is: {result}')

    # roll command
    # roll two dices, values will be 2-12
    # replies with a randomly generated value between 2-12
    # .roll
    @commands.command(name='roll')
    async def roll(self, ctx):
        roll = random.randint(2, 12)
        if len(str(roll)) == 1:
            rollMessage = str(roll)
            rollMessage += "\u20e3"
            await ctx.message.add_reaction(rollMessage)
        else:
            rollMessage = str(roll)[:1]
            rollMessage += "\u20e3"
            await ctx.message.add_reaction(rollMessage)
            rollMessage = str(roll % 10)
            rollMessage += "\u20e3"
            await ctx.message.add_reaction(rollMessage)

        await ctx.send(roll)
    
    # Lists all the commands that can be executed 
    # .help
    @commands.command(name='help')
    async def help(self, ctx):
        author = ctx.message.author

        embed = discord.Embed(
            colour = discord.Colour.orange()
        )

        embed.set_author(name='Commands')
        embed.add_field(name='.ping', value='Returns Pong!', inline=False)
        embed.add_field(name='.coolbot', value='Is the bot cool?', inline=False)
        embed.add_field(name='.getAvatar @user', value='Returns a users avatar.', inline=False)
        embed.add_field(name='.roll', value='roll two dices, values will be 2-12.', inline=False)

        await author.send('My Commands. :)', embed=embed)

# End of class BasicCog

# Add this cog to the bot
def setup(bot):
    bot.add_cog(BasicCog(bot))