from discord.ext import commands
import random


class ent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def chance(self, ctx):
        author = ctx.message.author  # получаем автора сообщения.
        ran = random.randint(0, 100)  # генерируем случайное число в диапозоне от 0 до 100 включительно.
        await ctx.channel.purge(limit=1)
        await ctx.send(f' {author.mention}' + ", " + str(ran) + "%")  # шлем в чат вероятность упоминая автора сообщения

    @commands.command()
    async def ask(self, ctx):
        ans = ['yes', 'no']  # создаем список, возможных ответов
        author = ctx.message.author  # получаем автора сообщения.
        onezero = random.randint(0, 1)  # получаем случайное число, для того чтобы вытащить случайный ответ из списка
        await ctx.channel.purge(limit=1)
        await ctx.send(f'{author.mention}' + ", " + ans[onezero])  # шлём в чат выполненную команду


def setup(bot):
    bot.add_cog(ent(bot=bot))
