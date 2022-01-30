import discord
from discord.ext import commands

class BootUp(commands.Cog):
    
    def __init__(self,client):
        self.client= client
    
    @commands.Cog.listener() #booting up
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game('games.'))
        print('We have logged in!')
        print('---------------------')

    @commands.command() #shutting down command
    @commands.is_owner()
    async def shutdown(self,ctx):
        await ctx.send(f"Shutting down.")
        await ctx.bot.logout()

    
def setup(client): #setup ca sa unesti cogul la bot
    client.add_cog(BootUp(client))