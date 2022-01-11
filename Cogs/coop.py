from discord.ext import commands
import json
import requests
from Main import Token

class coop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tube(self, ctx):
        author = ctx.message.author
        data = {
            "max_age": 86400,
            "max_uses": 0,
            "target_application_id": 880218394199220334,  # YouTube
            "target_type": 2,
            "temporary": False,
            "validate": None
        }
        headers = {
            "Authorization": "Bot {0}".format(Token) ,
            "Content-type": "application/json"
        }

        if ctx.author.voice is not None:
            if ctx.author.voice.channel is not None:
                channel = ctx.author.voice.channel.id
            else:
                await ctx.channel.purge(limit=1)
                await ctx.send("Please, join on the channel!")
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send("Please, join on the channel!")

        response = requests.post(f'https://discord.com/api/v8/channels/{channel}/invites', data=json.dumps(data),
                                 headers=headers)
        link = json.loads(response.content)

        await ctx.channel.purge(limit=1)
        await ctx.send(f'{author.mention}' + " " + f"https://discord.com/invite/{link['code']}")

    @commands.command()
    async def poker(self, ctx):
        author = ctx.message.author
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
                await ctx.channel.purge(limit=1)
                await ctx.send("Please, join on the channel!")
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send("Please, join on the channel!")

        response = requests.post(f'https://discord.com/api/v8/channels/{channel}/invites', data=json.dumps(data),
                                 headers=headers)
        link = json.loads(response.content)

        await ctx.channel.purge(limit=1)
        await ctx.send(f'{author.mention}' + " " + f"https://discord.com/invite/{link['code']}")

    @commands.command()
    async def Doodle(self, ctx):
        author = ctx.message.author
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
                await ctx.channel.purge(limit=1)
                await ctx.send("Please, join on the channel!")
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send("Please, join on the channel!")

        response = requests.post(f'https://discord.com/api/v8/channels/{channel}/invites', data=json.dumps(data),
                                 headers=headers)
        link = json.loads(response.content)

        await ctx.channel.purge(limit=1)
        await ctx.send(f'{author.mention}' + " " + f"https://discord.com/invite/{link['code']}")
    


def setup(bot):
    bot.add_cog(coop(bot=bot))
