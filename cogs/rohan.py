import discord
from discord.ext import commands


class Rohan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="rohan")
    async def rohan(self, ctx):
        role_name = "Rohirrim"
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        if role is None:
            await ctx.send("Volk nicht gefunden.")
            return

        try:
            await ctx.author.add_roles(role)
            await ctx.send(f"{ctx.author.mention} ist jetzt ein {role_name}.")
        except discord.Forbidden:
            await ctx.send("Ich habe keine Berechtigung, diese Rolle zu geben.")
        except discord.HTTPException:
            await ctx.send("Es ist ein Fehler beim Rollen-Update passiert.")


async def setup(bot):
    await bot.add_cog(Rohan(bot))
