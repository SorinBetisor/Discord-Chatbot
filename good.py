import discord,random
from discord.ext import commands

client= commands.Bot(command_prefix = '!')
@client.event
async def on_ready():
    print("We have logged in !")
    print("--------------------")

@client.event
async def on_member_join(member):
    print(f'{member} has joined our server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left our server. :(')

@client.command() #comanda hello
async def hello(ctx):
    username = str(ctx.author).split('#')[0]
    await ctx.send(f"Wassup {username}!")
    
@client.command() #ping
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command() #black
async def black(ctx):
    percentage=str(100- random.randint(0,100))
    username = str(ctx.author).split('#')[0]
    if int(percentage)>=50:
        race=",my nigga."
        only=""
    else:
        race=", you white boy."
        only="only "
    await ctx.send (f'{username}'+", you are "+only+percentage+f"% black"+race)

@client.command() #shutdown
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send(f"Shutting down, nibbers.")
    await ctx.bot.logout()

@client.command() #slap
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send('{} just got slapped for {}'.format(slapped, reason))

@client.command(aliases=['8ball']) #8ball
async def _8ball(ctx,*,question):
    responses=["It is certain.",
"It is decidedly so.",
"Without a doubt.",
"Yes - definitely.",
"You may rely on it.",
"As I see it, yes.",
"Most likely.",
"Outlook good.",
"Yes.",
"Signs point to yes.",
"Reply hazy, try again.",
"Ask again later.",
"Better not tell you now.",
"Cannot predict now.",
"Concentrate and ask again.",
"Don't count on it.",
"My reply is no.",
"My sources say no.",
"Outlook not so good.",
"Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command() #clear
@commands.is_owner()
async def clear(ctx,amount=2):
    await ctx.channel.purge(limit=amount)

@client.command() #kick
@commands.is_owner()
async def kick(ctx,member : discord.Member, *,reason=None):
    await member.kick(reason=reason)

@client.command() #ban
@commands.is_owner()
async def ban(ctx,member : discord.Member, *,reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@client.command() #unban
@commands.is_owner()
async def unban(ctx, *, member):
    banned_users= await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user= ban_entry.user

        if (user.name, user.discriminator)== (member_name,member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} unbanned.')
            return


client.run('OTMzNjg4MzA0OTU0NjUwNjY2.YelK_g.hjhIcbEtflfAXVJsO7Pz7QEjzuQ')