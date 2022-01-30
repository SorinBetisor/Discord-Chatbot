from asyncio import events #.///
import discord,random,os,json
from discord.ext import commands
from numpy import isin
from discord.utils import get
intents = discord.Intents.default() #gateway must be on
intents.members = True
def get_prefix(client,message):
        with open ('prefixes.json','r') as f:
            prefixes= json.load(f)

        return prefixes[str(message.guild.id)]
intents = discord.Intents().all()
client = commands.Bot(command_prefix= get_prefix,intents=intents)

@client.event
async def on_guild_join(guild): #when bot is invited
    with open ('prefixes.json','r') as f: #importa prefixurile
                prefixes= json.load(f)

    prefixes[str(guild.id)] = '!'

    with open('prefixes.json','w') as f: #exporta
        json.dump(prefixes,f)
@client.event #when bot is removed
async def on_guild_remove(guild):
    with open ('prefixes.json','r') as f: #importa prefixurile
                prefixes= json.load(f)

    prefixes.pop(str(guild.id)) #pops the id when removed

    with open('prefixes.json','w') as f: #exporta
        json.dump(prefixes,f)


@client.command()
@commands.is_owner()
async def load(ctx,extension): #load
    client.load_extension(f'cogs.{extension}' )
    await ctx.send('Loaded.')


@client.command()
@commands.is_owner()
async def unload(ctx,extension): #unload
    client.unload_extension(f'cogs.{extension}' )
    await ctx.send('Unloaded.')


@client.command()
@commands.is_owner()
async def reload(ctx,extension): #reload
    client.unload_extension(f'cogs.{extension}' )
    client.load_extension(f'cogs.{extension}' )
    await ctx.send('Reloaded.')

@client.event #automatic member role assigment
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name='Member')
    await member.add_roles(role)

for filename in os.listdir('./cogs'): #checking cogs file
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#///////////ERROR HANDLING////////////////
@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandNotFound):  
        await ctx.send('Invalid command used.')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify the required argument.')
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send('Not enough permissions. ')
client.run('OTMzNjg4MzA0OTU0NjUwNjY2.YelK_g.9qFKg3sCha2QQK178K-xp4M0Cys')