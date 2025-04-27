import discord
from discord.ext import commands
from datetime import datetime
from datetime import datetime, timezone


class Userinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="info")
    async def userinfo(self, ctx, member: discord.Member = None):
        # Falls kein User angegeben wird, nimm den Befehlssender selbst
        if member is None:
            member = ctx.author

        # Rollen zusammenfassen
        roles = [role.mention for role in member.roles if role.name != "@everyone"]
        roles_display = ", ".join(roles) if roles else "Keine Rollen"

        # Embed erstellen
        embed = discord.Embed(
            title=f"Infos über {member}",
            description=f"Hier sind die Details zu {member.mention}",
            color=discord.Color.blue(),
            timestamp=datetime.now(timezone.utc),
        )
        embed.set_thumbnail(
            url=member.avatar.url if member.avatar else discord.Embed.Empty
        )

        embed.add_field(
            name="Username", value=f"{member.name}#{member.discriminator}", inline=True
        )
        embed.add_field(name="ID", value=member.id, inline=True)
        embed.add_field(
            name="Beigetreten am",
            value=member.joined_at.strftime("%d.%m.%Y %H:%M:%S"),
            inline=False,
        )
        embed.add_field(
            name="Account erstellt am",
            value=member.created_at.strftime("%d.%m.%Y %H:%M:%S"),
            inline=False,
        )
        embed.add_field(name="Rollen", value=roles_display, inline=False)

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Userinfo(bot))
