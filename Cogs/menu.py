import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle
from Main import *
import json
import random
import requests


class menu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def menu(self, ctx):
        author = ctx.message.author
        await ctx.send(
            embed=discord.Embed(title=f'{author}' + ", ""Welcome to the menu!"),
            components=[
                [Button(style=ButtonStyle.gray, label="Tube", emoji="▶"),
                 Button(style=ButtonStyle.gray, label="Poker", emoji="🃏"),
                 Button(style=ButtonStyle.gray, label="Doodle", emoji="🖌️")],
                [Button(style=ButtonStyle.gray, label="Chance", emoji="🎲"),
                 Button(style=ButtonStyle.gray, label="Ask", emoji="❓"),
                 Button(style=ButtonStyle.gray, label="Clear 10 messages", emoji="🧹")],
            ],
        )

        response = await bot.wait_for("button_click")
        if response.channel == ctx.channel:
            if response.component.label == "Tube":
                data = {
                    "max_age": 86400,
                    "max_uses": 0,
                    "target_application_id": 755600276941176913,  # YouTube
                    "target_type": 2,
                    "temporary": False,
                    "validate": None
                }
                headers = {
                    "Authorization": "Bot {0}".format(Token),
                    "Content-type": "application/json"
                }

                if ctx.author.voice is not None:
                    if ctx.author.voice.channel is not None:
                        channel = ctx.author.voice.channel.id
                    else:
                        await ctx.channel.purge(limit=2)
                        await ctx.send("Please, join on the channel!")
                        await response.edit_origin()
                else:
                    await ctx.channel.purge(limit=2)
                    await ctx.send("Please, join on the channel!")
                    await response.edit_origin()

                responses = requests.post(f'https://discord.com/api/v8/channels/{channel}/invites',
                                          data=json.dumps(data),
                                          headers=headers)
                link = json.loads(responses.content)

                await ctx.channel.purge(limit=2)
                await ctx.send(f'{author.mention}' + " " + f"https://discord.com/invite/{link['code']}")
                await response.edit_origin()

            elif response.component.label == "Poker":
                data = {
                    "max_age": 86400,
                    "max_uses": 0,
                    "target_application_id": 755827207812677713,  # Poker
                    "target_type": 2,
                    "temporary": False,
                    "validate": None
                }
                headers = {
                    "Authorization": "Bot {0}".format(Token),
                    "Content-type": "application/json"
                }

                if ctx.author.voice is not None:
                    if ctx.author.voice.channel is not None:
                        channel = ctx.author.voice.channel.id
                    else:
                        await ctx.channel.purge(limit=2)
                        await ctx.send("Please, join on the channel!")
                        await response.edit_origin()
                else:
                    await ctx.channel.purge(limit=2)
                    await ctx.send("Please, join on the channel!")
                    await response.edit_origin()

                responses = requests.post(f'https://discord.com/api/v8/channels/{channel}/invites',
                                          data=json.dumps(data),
                                          headers=headers)
                link = json.loads(responses.content)

                await ctx.channel.purge(limit=2)
                await ctx.send(f'{author.mention}' + " " + f"https://discord.com/invite/{link['code']}")
                await response.edit_origin()

            elif response.component.label == "Doodle":
                data = {
                    "max_age": 86400,
                    "max_uses": 0,
                    "target_application_id": 878067389634314250,  # Doodle
                    "target_type": 2,
                    "temporary": False,
                    "validate": None
                }
                headers = {
                    "Authorization": "Bot {0}".format(Token),
                    "Content-type": "application/json"
                }

                if ctx.author.voice is not None:
                    if ctx.author.voice.channel is not None:
                        channel = ctx.author.voice.channel.id
                    else:
                        await ctx.channel.purge(limit=2)
                        await ctx.send("Please, join on the channel!")
                        await response.edit_origin()
                else:
                    await ctx.channel.purge(limit=2)
                    await ctx.send("Please, join on the channel!")
                    await response.edit_origin()

                responses = requests.post(f'https://discord.com/api/v8/channels/{channel}/invites',
                                          data=json.dumps(data),
                                          headers=headers)
                link = json.loads(responses.content)

                await ctx.channel.purge(limit=2)
                await ctx.send(f'{author.mention}' + " " + f"https://discord.com/invite/{link['code']}")
                await response.edit_origin()

            elif response.component.label == "Clear 10 messages":
                messages = await ctx.channel.purge(limit=10)  # пурджим сообщения, +1 т.к. наше тоже удалится
                await ctx.channel.purge(limit=2)
                await ctx.send(f"{len(messages)} messages were deleted")  # оповещяем об удалении и количестве сообщений
                await response.edit_origin()

            elif response.component.label == "Chance":
                author = ctx.message.author  # получаем автора сообщения.
                ran = random.randint(0, 100)  # генерируем случайное число в диапозоне от 0 до 100 включительно.
                await ctx.channel.purge(limit=2)
                await ctx.send(
                    f' {author.mention}' + ", " + str(ran) + "%")  # шлем в чат вероятность упоминая автора сообщения
                await response.edit_origin()

            elif response.component.label == "Ask":
                ans = ['yes', 'no']  # создаем список, возможных ответов
                author = ctx.message.author  # получаем автора сообщения.
                onezero = random.randint(0,
                                         1)  # получаем случайное число, для того чтобы вытащить случайный ответ из списка
                await ctx.channel.purge(limit=2)
                await ctx.send(f'{author.mention}' + ", " + ans[onezero])  # шлём в чат выполненную команду
                await response.edit_origin()


def setup(bot):
    bot.add_cog(menu(bot=bot))
