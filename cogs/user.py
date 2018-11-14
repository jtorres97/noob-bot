import discord
from discord.ext import commands

class UserCog:
    def __init__(self, bot):
        self.bot = bot

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
    
    # Gives User Information
    # .info @user
    @commands.command(name='info')
    async def info(self,ctx, user: discord.Member):
        embed = discord.Embed(title='User Info', image=user.avatar, colour=user.colour)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="Username: ", value=user.name, inline=True)
        embed.add_field(name="Join Date: ", value=user.joined_at,inline=True)
        embed.add_field(name="Display name: ", value=user.display_name,inline=True)
        embed.add_field(name="Account Created at: ",value=user.created_at,inline=True)
        await ctx.send(embed=embed)

    # Lists every member in the server, along with their discord id
    # .listMembers
    @commands.command(name="listMembers")
    async def listMembers(self, ctx):
        member_string = "\n"
        for member in ctx.guild.members:
            member_string += ("\t" + '{:32}'.format(member.name) + ":\t(id = " + str(member.id) + ")\n")
        server_string = "Server Name: {}\nMembers:\n    ".format(ctx.guild.name)
        result = "```"
        result += ("\n" + server_string + member_string)
        result += ("\n```")
        await ctx.send(result)

# End of class UserCog

# Add this cog to the bot
def setup(bot):
    bot.add_cog(UserCog(bot))
