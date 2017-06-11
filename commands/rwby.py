from discord.ext import commands

class RWBY():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def scream(self, ctx):
        """AAAAAAAAAAAAAAAAAAAA"""
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, "assets/imgs/scream.jpg")

    @commands.command(pass_context=True)
    async def heil(self, ctx):
        """sieg heil"""
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, "assets/imgs/blake_heil.png")

    @commands.command(pass_context=True)
    async def waifu(self, ctx):
        """Pep's Waifu"""
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, "assets/imgs/waifu.png")

def setup(bot):
    bot.add_cog(RWBY(bot))
