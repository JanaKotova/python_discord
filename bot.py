import discord
from discord.ext import commands

bot = discord.Client()

TOKEN = "Ваш токен"

@bot.event
async def on_message(message):
 if message.author == bot.user:
  return
 if message.content == ("?help") or message.content == ("?команды") or message.content == ("?помощь"):
  await message.channel.send("Список команд:\n1.) Команда\n2.) Команда")

bot.run(TOKEN)
