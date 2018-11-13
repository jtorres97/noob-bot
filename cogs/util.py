import discord
from discord.ext import commands

class UtilCog():
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

    # A simple command which only responds to the owner of the bot
    # .me
    @commands.command(name='me')
    @commands.is_owner()
    async def only_me(self, ctx):
        await ctx.send(f'Hello {ctx.author.mention}. This command can only be used by you!')

# End of class BasicCog

# Add this cog to the bot
def setup(bot):
    bot.add_cog(UtilCog(bot))
