import discord
from discord.ext import commands
import asyncio


class TempVC(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.temp_channels = []

    @commands.command()
    async def tempvc(
        self, ctx, category_name: str, *, channel_name: str = "Temporärer Raum"
    ):
        category = discord.utils.get(ctx.guild.categories, name=category_name)

        if not category:
            await ctx.send("Kategorie nicht gefunden.")
            categories = [category.name for category in ctx.guild.categories]
            await ctx.send(f"Verfügbare Kategorien: {', '.join(categories)}")
            return

        temp_channel = await ctx.guild.create_voice_channel(
            channel_name, category=category
        )
        await ctx.send(
            f"Temporärer Raum {temp_channel.name} wurde erstellt, in der Kategorie {category.name}."
        )

        self.temp_channels.append(temp_channel.id)  # save dc voice channel id
        await asyncio.sleep(30)  # delete after 30 seconds if it has no member inside

        if len(temp_channel.members) == 0:
            await temp_channel.delete()
            await ctx.send(f"Temporärer Raum {temp_channel.name} wurde gelöscht.")

        else:
            await ctx.send(f"Temporärer Raum {temp_channel.name} wurde nicht gelöscht.")

        @commands.Cog.listener()
        async def on_voice_state_update(self, member, before, after):
            if before.channel and before.channel.id in self.temp_channels:
                channel = before.channel
                if len(channel.members) == 0:
                    await channel.delete()
                    await ctx.send(f"Temporärer Raum {channel.name} wurde gelöscht.")


async def setup(bot):
    await bot.add_cog(TempVC(bot))
