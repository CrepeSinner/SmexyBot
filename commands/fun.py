import asyncio
import cat
import random
import os
import json

from discord.ext import commands
from utils.tools import *
from utils.unicode import *
from utils.fun.lists import *
from utils import imagetools
from PIL import Image
#from cleverbot import Cleverbot


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        #self.cb = Cleverbot()

    @commands.command(pass_context=True)
    async def cat(self, ctx):
        """Sends a random cute catto gif because cats are soooo cuteeee <3 >.<"""
        await self.bot.send_typing(ctx.message.channel)
        cat.getCat(directory="data", filename="cat", format="gif")
        await asyncio.sleep(1) # This is so the bot has enough time to download the file
        await self.bot.send_file(ctx.message.channel, "data/cat.gif")
        # Watch Nero spam this command until the bot crashes

    @commands.command()
    async def nicememe(self):
        """Nice Meme!"""
        await self.bot.say("http://niceme.me")

    @commands.command(pass_context=True)
    async def spam(self, ctx):
        """SPAM SPAM SPAM"""
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, "assets/imgs/spam.png")

    @commands.command(pass_context=True)
    async def quoteaf(self, ctx):
        """Don't quote me on that"""
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, "assets/imgs/quotes/{}.png".format(random.randint(1, len([file for file in os.listdir("assets/imgs/quotes")]))))

    @commands.command(pass_context=True)
    async def b1nzy(self, ctx):
        """b1nzy pls no ;-;"""
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, "assets/imgs/b1nzy_with_banhammer.png")

    @commands.command()
    async def sombra(self):
        """Boop me Sombra <3"""
        await self.bot.say(sombra)

    @commands.command()
    async def lenny(self):
        """<Insert lenny face here>"""
        await self.bot.say(lenny)

    @commands.command()
    async def psat(self):
        """Please."""
        await self.bot.say(random.choice(psat_memes))

    @commands.command(pass_context=True)
    async def hoodaf(self, ctx):
        """Me in my hood"""
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, "assets/imgs/TheHood.gif")
        await self.bot.say("I look good in a hood, amirite?")

    @commands.command()
    async def actdrunk(self):
        """I got drunk on halloween in 2016 it was great"""
        await self.bot.say(random.choice(drunkaf))

    @commands.command(pass_context=True)
    async def rate(self, ctx, user:discord.User=None):
        """Have the bot rate yourself or another user (rigged af)"""
        if user is None or user.id == ctx.message.author.id:
            await self.bot.say("I rate you a 10/10")
        elif user == self.bot.user:
            await self.bot.say("I rate myself a -1/10")
        else:
            await self.bot.say("I rate {} a {}/10".format(user.name, random.randint(0, 10)))

    @commands.command()
    async def honk(self):
        """Honk honk mother fucka"""
        await self.bot.say(random.choice(honkhonkfgt))

    @commands.command(pass_context=True)
    async def quote(self, ctx, id:str):
        """Quotes a message with the specified message ID"""
        message = await self.bot.get_message(ctx.message.channel, id)
        if message is None:
            await self.bot.say("I could not find a message with an ID of `{}` in this channel".format(id))
            return
        embed = make_message_embed(message.author, message.author.color, message.content, formatUser=True)
        embed.timestamp = message.timestamp
        await self.bot.say(embed=embed)

    @commands.command()
    async def spellout(self, *, msg:str):
        """S P E L L O U T"""
        await self.bot.say(" ".join(list(msg.upper())))

    @commands.command(pass_context=True)
    async def trigger(self, ctx, *, member:discord.Member=None):
        """Triggers a user"""
        await self.bot.send_typing(ctx.message.channel)
        if member is None:
            member = ctx.message.author
        download_file(get_avatar(member, animate=False), "data/trigger.png")
        avatar = Image.open("data/trigger.png")
        triggered = imagetools.rescale(Image.open("assets/imgs/pillow/triggered.jpg"), avatar.size)
        position = 0, avatar.getbbox()[3] - triggered.getbbox()[3]
        avatar.paste(triggered, position)
        avatar.save("data/trigger.png")
        await self.bot.send_file(ctx.message.channel, "data/trigger.png")

    @commands.command(pass_context=True)
    async def blackandwhite(self, ctx, user:discord.Member=None):
        """Turns your avatar or the specified user's avatar black and white"""
        await self.bot.send_typing(ctx.message.channel)
        if user is None:
            user = ctx.message.author
        download_file(get_avatar(user, animate=False), "data/blackandwhite.png")
        avatar = Image.open("data/blackandwhite.png").convert("L")
        avatar.save("data/blackandwhite.png")
        await self.bot.send_file(ctx.message.channel, "data/blackandwhite.png")

    @commands.command(pass_context=True)
    async def headpat(self, ctx):
        """You have recieved a pat"""
        await self.bot.send_typing(ctx.message.channel)

    @commands.command()
    async def reverse(self, *, msg:str):
        """ffuts esreveR"""
        await self.bot.say(msg[::-1])

    @commands.command(pass_context=True)
    async def fujoshi(self, ctx):
        """gud shit"""
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, "assets/imgs/fujoshi.png")

    @commands.command(pass_context=True)
    async def frork(self, ctx):
        """frork"""
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, "assets/imgs/frok.png")
        await self.bot.say("Release! The! Frork!")

    @commands.command(pass_context=True)
    async def semehands(self, ctx):
        """semehands"""
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, "assets/imgs/semehands.png")
        await self.bot.say("SEME!")

    @commands.command(pass_context=True)
    async def breadandbutter(self, ctx):
        """breadandbutter"""
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, "assets/imgs/breadandbutter.png")
        await self.bot.say("The Butter go on top of The Bread!")

    @commands.command(pass_context=True)
    async def jesus(self, ctx):
        """jesus"""
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, "assets/imgs/jesus.jpg")

    @commands.command(pass_context=True)
    async def kegs(self, ctx):
        """kegs"""
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, "assets/imgs/kegs.png")

    @commands.command(pass_context=True)
    async def sendnewts(self, ctx):
        """send me newts"""
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, "assets/imgs/newts.png")
        await self.bot.say("Send me newts, yeh?!")

    @commands.command(pass_context=True)
    async def newts(self, ctx):
        """send me newts"""
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, "assets/imgs/newts/{}.jpg".format(random.randint(1, len([file for file in os.listdir("assets/imgs/newts")]))))

    @commands.command(pass_context=True)
    async def lemmesmash(self, ctx):
        """send me newts"""
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, "assets/imgs/lemmesmash.gif")
        await self.bot.say("You want sum fuk?")

def setup(bot):
    bot.add_cog(Fun(bot))
