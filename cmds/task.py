import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, asyncio, datetime

class Task(Cog_Extension):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.counter = 0

        async def time_interval():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel("Your Channel ID")
            while not self.bot.is_closed():
                now_time = datetime.datetime.now().strftime('%H%M')
                with open('setting.json', 'r', encoding='utf8') as jfile:
                    jdata = json.load(jfile)
                if now_time == jdata['time'] and self.counter == 0:
                    await self.channel.send('안녕하세요')
                    self.counter = 1
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
                    pass

        self.bg_task = asyncio.create_task(time_interval())

    @commands.command()
    async def set_channel(self, ctx, ch:int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'Set Channel: {self.channel.mention}')

    @commands.command()
    async def set_time(self, ctx, time):
        self.counter = 0
        with open('setting.json', 'r', encoding='utf8') as jfile:
            jdata = json.load(jfile)
        jdata['time'] = time
        with open('setting.json', 'w', encoding='utf8') as jfile:
            json.dump(jdata, jfile, indent=4)


async def setup(bot):
    await bot.add_cog(Task(bot))
