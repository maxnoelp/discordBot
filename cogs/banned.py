import discord
from discord.ext import commands


class BannedFromLOTR(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="banned")
    @commands.has_permissions(administrator=True)
    async def banned(self, ctx, member: discord.Member):
        role_rohan = discord.utils.get(ctx.guild.roles, name="Rohirrim")
        role_gondor = discord.utils.get(ctx.guild.roles, name="Soldat Gondors")
        if role_rohan is None or role_gondor is None:
            await ctx.send("Die Rolle Rohirrim existiert nicht.")
            return

        if role_rohan in member.roles:
            await member.remove_roles(role_rohan)
            await ctx.send(f"{member.mention} ist jetzt nicht mehr ein Rohirrim.")
        elif role_gondor in member.roles:
            await member.remove_roles(role_gondor)
            await ctx.send(f"{member.mention} ist jetzt nicht mehr ein Soldat Gondors.")
        else:
            await ctx.send(f"{member.mention} ist kein Rohirrim.")


async def setup(bot):
    await bot.add_cog(BannedFromLOTR(bot))
