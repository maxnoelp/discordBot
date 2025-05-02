import discord
from discord.ext import commands


class KingOfRohan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="KingOfRohan")
    @commands.has_permissions(administrator=True)
    async def KingOfRohan(self, ctx):
        role_name = "König von Rohan"
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        if role is None:
            await ctx.send("Rolle nicht gefunden.")
            return

        # rolle kann nur ein Admin geben
        try:
            await ctx.author.add_roles(role)
            await ctx.send(f"{ctx.author.mention} ist jetzt der {role_name}.")
        except discord.Forbidden:
            await ctx.send("Ich habe keine Berechtigung, diese Rolle zu geben.")
        except discord.HTTPException:
            await ctx.send("Es ist ein Fehler beim Rollen-Update passiert.")


async def setup(bot):
    await bot.add_cog(KingOfRohan(bot))
