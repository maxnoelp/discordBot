import discord
import os
import asyncio
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv.get("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.guilds = True
intents.voice_states = True
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")


async def main():
    async with bot:
        await bot.load_extension("cogs.tempvc")
        await bot.load_extension("cogs.user_info")
        await bot.load_extension("cogs.rohan")
        await bot.load_extension("cogs.banned")
        await bot.load_extension("cogs.gondor")
        await bot.load_extension("cogs.king_of_rohan")
        await bot.load_extension("cogs.temp_voice_create")
        await bot.start(TOKEN)


asyncio.run(main())
