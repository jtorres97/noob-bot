import discord
from discord.ext import commands

import traceback
import random

class BasicCog:
    def __init__(self, bot):
        self.bot = bot

    # Reloads an extension in the bot
    # .reload 
    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, name: str):
        m = await ctx.send(f'Loading {name}')
        try:
            self.bot.unload_extension(f'cogs.{name}')
            self.bot.load_extension(f'cogs.{name}')
            await m.edit(content='Extension reloaded.')
        except (ImportError, SyntaxError, discord.ClientException) as e:
            stack_line = str(e).split('\n')[-1]
            await m.edit(content=f'Error while loading {name}\n`{stack_line}`')

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
        embed.add_field(name='.roll', value='Roll two dices, values will be 2-12.', inline=False)
        embed.add_field(name='.info @user', value='Gives information about a user.', inline=False)
        embed.add_field(name='.rps', value='Play a game of Rock, Paper, Scissors with the bot.', inline=False)

        await author.send('My Commands. :)', embed=embed)

    # Gives User Information
    # .info @user
    @commands.command()
    async def info(self,ctx, user: discord.Member):
        embed = discord.Embed(title='User Info', image=user.avatar, colour=user.colour)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="Username: ", value=user.name, inline=True)
        embed.add_field(name="Join Date: ", value=user.joined_at,inline=True)
        embed.add_field(name="Display name: ", value=user.display_name,inline=True)
        embed.add_field(name="Account Created at: ",value=user.created_at,inline=True)
        await ctx.send(embed=embed)

    # Play a game of Rock, Paper, Scissors with the bot.
    # .rps
    @commands.command()
    async def rps(self, ctx, userChoice : str):
        vals = ["rock", "paper", "scissors"]
        userChoice = str.lower(userChoice)
        if userChoice not in vals:
            await ctx.send(ctx.author.mention + " Invalid input. Please enter \"rock\", \"paper\", or \"scissors\"")
        else:
            botChoice = vals[random.randint(0, 2)]
            if(userChoice == "rock" and botChoice == "paper"):
                await ctx.send(f"I choose {botChoice}! {ctx.author.mention}... You lose! " + u"\U0001F602")
            elif(userChoice == "rock" and botChoice == "scissors"):
                await ctx.send(f"I choose {botChoice}! {ctx.author.mention}... You win! " + u"\U0001F614")
            elif(userChoice == "paper" and botChoice == "rock"):
                await ctx.send(f"I choose {botChoice}! {ctx.author.mention}... You win! " + u"\U0001F614")  
            elif(userChoice == "paper" and botChoice == "scissors"):
                await ctx.send(f"I choose {botChoice}! {ctx.author.mention}... You lose! " + u"\U0001F602")  
            elif(userChoice == "scissors" and botChoice == "rock"):
                await ctx.send(f"I choose {botChoice}! {ctx.author.mention}... You lose! " + u"\U0001F602")
            elif(userChoice == "scissors" and botChoice == "paper"):
                await ctx.send(f"I choose {botChoice}! {ctx.author.mention}... You win! " + u"\U0001F614")
            else:
                await ctx.send(ctx.author.mention + " It's a tie " + "\uD83D\uDD2B")

# End of class BasicCog

# Add this cog to the bot
def setup(bot):
    bot.add_cog(BasicCog(bot))