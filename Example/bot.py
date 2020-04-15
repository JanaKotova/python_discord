import discord
from discord.ext import commands
import random

bot = discord.Client()

TOKEN = "Ваш токен"

@bot.event
async def on_message(message):
 if message.author == bot.user:
  return
 if message.content.lower() == ("?help"):
  await message.channel.send("Список команд:\n1.) ?random\n2.) ?скоро")
 if message.content.lower() == ("?random"):
  await message.channel.send(random.randint(0,10))
bot.run(TOKEN)