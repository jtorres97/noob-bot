import discord
from discord.ext import commands

import traceback

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
        embed.add_field(name='.roll', value='Roll two dices, values will be 2-12.', inline=False)
        embed.add_field(name='.info @user', value='Gives information about a user.', inline=False)
        embed.add_field(name='.rps', value='Play a game of Rock, Paper, Scissors with the bot.', inline=False)

        await author.send('My Commands. :)', embed=embed)

# End of class BasicCog

# Add this cog to the bot
def setup(bot):
    bot.add_cog(BasicCog(bot))