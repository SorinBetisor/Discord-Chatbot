import discord,random
import json
from discord.ext import commands
class OwnerCommands(commands.Cog):
    
    def __init__(self,client):
        self.client= client
    
    @commands.command()
    @commands.is_owner()
    async def changeprefix(self,ctx,prefix):
        with open ('prefixes.json','r') as f: #importa prefixurile
                    prefixes= json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open('prefixes.json','w') as f: #exporta
            json.dump(prefixes,f)
        
        await ctx.send(f'The prefix was changed to {prefix}')

    


def setup(client): #setup ca sa unesti cogul la bot
    client.add_cog(OwnerCommands(client))