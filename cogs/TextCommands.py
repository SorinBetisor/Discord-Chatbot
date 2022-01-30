import discord,random
from discord.ext import commands
class TextCommands(commands.Cog):
    
    def __init__(self,client):
        self.client= client
    
    @commands.command() #ping
    async def ping(self,ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')
    
    @commands.command() #hello
    async def hello(self,ctx):
        username = str(ctx.author).split('#')[0]
        await ctx.send(f"Wassup {username}!")

    @commands.command() #black
    async def black(self,ctx):
        percentage=str(100- random.randint(0,100))
        username = str(ctx.author).split('#')[0]
        if int(percentage)>=50:
            race=",my nigga."
            only=""
        else:
            race=", you white boy."
            only="only "
        await ctx.send (f'{username}'+", you are "+only+percentage+f"% black"+race)

    @commands.command() #slap
    async def slap(self,ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
        slapped = ", ".join(x.name for x in members)
        if slapped=='':
            await ctx.send('Who?')
            return
        await ctx.send('{} just got slapped for {}'.format(slapped, reason))

    @commands.command(aliases=['8ball']) #8ball
    async def _8ball(self,ctx,*,question):
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


def setup(client): #setup ca sa unesti cogul la bot
    client.add_cog(TextCommands(client))