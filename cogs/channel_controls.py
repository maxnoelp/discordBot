import discord
from discord import ui, Interaction, ButtonStyle
import asyncio


class ChannelControlView(ui.View):
    def __init__(
        self,
        owner: discord.Member,
        voice_channel: discord.VoiceChannel,
        text_channel: discord.TextChannel,
    ):
        super().__init__(timeout=None)
        self.owner = owner
        self.voice_channel = voice_channel
        self.text_channel = text_channel

    def is_owner(self, user):
        return user.id == self.owner.id

    @ui.button(label="📝 Name ändern", style=ButtonStyle.primary)
    async def rename_channel(self, interaction: Interaction, button: ui.Button):
        if not self.is_owner(interaction.user):
            return await interaction.response.send_message(
                "❌ Du darfst diesen Channel nicht bearbeiten.", ephemeral=True
            )

        await interaction.response.send_message(
            "📥 Bitte gib den neuen Namen ein:", ephemeral=True
        )

        def check(m):
            return m.author == interaction.user and m.channel == interaction.channel

        try:
            msg = await interaction.client.wait_for("message", check=check, timeout=30)
            await self.voice_channel.edit(name=msg.content)
            await self.text_channel.edit(name=f"text-{msg.content}")
            await msg.reply("✅ Kanalname geändert.")
        except asyncio.TimeoutError:
            await interaction.followup.send("⏱️ Zeit abgelaufen.", ephemeral=True)

    @ui.button(label="👥 Userlimit setzen", style=ButtonStyle.secondary)
    async def set_user_limit(self, interaction: Interaction, button: ui.Button):
        if not self.is_owner(interaction.user):
            return await interaction.response.send_message(
                "❌ Du darfst diesen Channel nicht bearbeiten.", ephemeral=True
            )

        await interaction.response.send_message(
            "📥 Bitte gib die maximale Anzahl an Nutzern ein (0 = unbegrenzt):",
            ephemeral=True,
        )

        def check(m):
            return m.author == interaction.user and m.channel == interaction.channel

        try:
            msg = await interaction.client.wait_for("message", check=check, timeout=30)
            limit = int(msg.content)
            await self.voice_channel.edit(user_limit=limit)
            await msg.reply(f"✅ Limit auf {limit} gesetzt.")
        except (asyncio.TimeoutError, ValueError):
            await interaction.followup.send(
                "❌ Ungültige Eingabe oder Zeit abgelaufen.", ephemeral=True
            )
