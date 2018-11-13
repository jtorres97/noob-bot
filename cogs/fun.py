import discord
from discord.ext import commands

import random

class FunCog():
    def __init__(self, bot):
        self.bot = bot

    # Is the bot cool?
    # .coolbot
    @commands.command(name='coolbot')
    async def cool_bot(self, ctx):
        await ctx.send('This bot is cool. :)')

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

# End of class FunCog

# Add this cog to the bot
def setup(bot):
    bot.add_cog(FunCog(bot))