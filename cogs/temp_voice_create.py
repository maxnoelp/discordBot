import discord
from discord.ext import commands
import asyncio
from cogs.channel_controls import ChannelControlView


class TempVoiceCreate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.voice_creator_channel_id = 1100476114813603971
        self.temp_channels = {}

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if after.channel and after.channel.id == self.voice_creator_channel_id:
            guild = member.guild
            category = after.channel.category
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                member: discord.PermissionOverwrite(read_messages=True),
                guild.me: discord.PermissionOverwrite(
                    read_messages=True, send_messages=True
                ),
            }
            temp_channel = await guild.create_voice_channel(
                name=f"Raum von {member.display_name}",
                category=category,
                overwrites=overwrites,
            )

            self.temp_channels[member.id] = temp_channel.id
            await member.move_to(temp_channel)
            text_channel = await guild.create_text_channel(
                name=f"text-{member.display_name}",
                category=category,
                overwrites={
                    guild.default_role: discord.PermissionOverwrite(
                        read_messages=False
                    ),
                    member: discord.PermissionOverwrite(read_messages=True),
                    guild.me: discord.PermissionOverwrite(
                        read_messages=True, send_messages=True
                    ),
                },
            )

            embed = discord.Embed(
                title="🎛️ Kanalsteuerung",
                description=f"{member.mention}, verwalte deinen Channel hier:",
                color=discord.Color.blurple(),
            )
            view = ChannelControlView(member, temp_channel, text_channel)
            await text_channel.send(embed=embed, view=view)

            await self.check_if_empty(temp_channel, text_channel)

    async def check_if_empty(self, channel, text_channel):
        await asyncio.sleep(10)
        while True:
            await asyncio.sleep(10)
            if len(channel.members) == 0:
                await channel.delete()
                try:
                    await text_channel.delete()
                except Exception as e:
                    print(f"TextChannel konnte nicht gelöscht werden: {e}")
                break


async def setup(bot):
    await bot.add_cog(TempVoiceCreate(bot))
