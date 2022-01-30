import discord,random,asyncio
from discord.ext import commands
class DurationConverter(commands.Converter):
    async def convert(self,ctx,argument):
        amount= argument[:-1]
        unit= argument[-1]

        possibleunits=['s','m','h','d']
        if amount.isdigit() and unit in possibleunits:
            return (int(amount), unit)

        raise commands.BadArgument(message='Not a valid duration')
class AdminCommands(commands.Cog):
    
    def __init__(self,client):
        self.client= client

    @commands.command() #kick
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx,member : commands.MemberConverter, *,reason=None):
        await member.kick(reason=reason)

    @commands.command() #tempban
    @commands.has_permissions(ban_members=True)
    async def tempban(self,ctx,member: commands.MemberConverter, duration: DurationConverter,*,reason=None):
        multiplier= {'s':1,'m':60,'h':3600,'d':86400}
        amount,unit= duration

        await member.ban(duration= duration,reason=reason)
        await ctx.send(f'{member} has been banned. The duration is = {amount}{unit}')
        await asyncio.sleep(amount*multiplier[unit])
        await ctx.guild.unban(member)
    @commands.command() #ban
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx,member : commands.MemberConverter, *,reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention} for {reason}')

    @commands.command() #unban
    @commands.has_permissions(ban_members=True)
    async def unban(self,ctx, *, member):
        banned_users= await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user= ban_entry.user

            if (user.name, user.discriminator)== (member_name,member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.mention} unbanned.')
                return

    @commands.command() #clear
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx,amount=2):
        await ctx.channel.purge(limit=amount)


def setup(client): #setup ca sa unesti cogul la bot
    client.add_cog(AdminCommands(client))