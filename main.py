import discord
from discord.ext import commands
from discord import app_commands

client = commands.Bot(command_prefix = "", intents=discord.Intents.all())

@client.event
async def on_ready():
  await client.tree.sync()
  print(f"Launched as {client.user.name}")

@client.tree.command(name = "info", description = "View information for this bot")
async def _info(ctx: discord.Interaction):
  await ctx.response.send_message("""

Official BetterSEQTA+ Discord Bot.

Can be used to push themes to the BetterSEQTA+ Repo.

-# Created by `ar-cyber`""")

client.run(open(".env", "r").read())
