import discord
from discord.ext import commands
import os 

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
img_name = "m2.png"
@bot.command()
async def mem(ctx):
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
bot.run("TOKEN")



