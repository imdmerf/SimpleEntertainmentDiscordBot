import discord
from Config import Token
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle
import os


bot = discord.Client()
bot = commands.Bot(command_prefix=".", case_insensitive=True)
bot.remove_command("help")

owner = Enter your discordId

@bot.event
async def on_ready():
    DiscordComponents(bot)
    print('Bot online: {0.user}'.format(bot))  # состояние бота


for filename in os.listdir('./Cogs'):  # подгружаем все .py файлы из папки 'Cogs'
    if filename.endswith('.py'):
        bot.load_extension(f"Cogs.{filename[:-3]}")


@bot.command()
async def load(ctx, extension):  # прописываем команду подгрузки когов
    if ctx.author.id == owner:
        bot.load_extension(f"Cogs.{extension}")
        await ctx.channel.purge(limit=1)
        await ctx.send("Cog is loaded")
    else:
        await ctx.channel.purge(limit=1)
        await ctx.send("Access denied")  # в случаи несовпадения айди запрещает доступ


@bot.command()
async def unload(ctx, extension):  # прописываем команду выгрузки когов
    if ctx.author.id == owner:
        bot.unload_extension(f"Cogs.{extension}")
        await ctx.channel.purge(limit=1)
        await ctx.send("Cog is unloaded")
    else:
        await ctx.channel.purge(limit=1)
        await ctx.send("Access denied")  # в случаи несовпадения айди запрещает доступ


@bot.command()
async def reload(ctx, extension):  # прописываем команду перезагрузки когов
    if ctx.author.id == owner:
        bot.reload_extension(f"Cogs.{extension}")
        await ctx.channel.purge(limit=1)
        await ctx.send("Cog is reloaded")
    else:
        await ctx.channel.purge(limit=1)
        await ctx.send("Access denied")  # в случаи несовпадения айди запрещает доступ


bot.run(Token)
