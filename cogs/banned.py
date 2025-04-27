import discord
from discord.ext import commands


class BannedFromLOTR(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="banned")
    @commands.has_permissions(administrator=True)
    async def banned(self, ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="Rohirrim")
        if role is None:
            await ctx.send("Die Rolle Rohirrim existiert nicht.")
            return

        if role in member.roles:
            await member.remove_roles(role)
            await ctx.send(f"{member.mention} ist jetzt nicht mehr ein Rohirrim.")
        else:
            await ctx.send(f"{member.mention} ist kein Rohirrim.")


async def setup(bot):
    await bot.add_cog(BannedFromLOTR(bot))
