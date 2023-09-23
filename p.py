import discord
from discord.ext import commands
import random
import os 

intents = discord.Intents.all()

bot = commands.Bot(intents=intents, command_prefix="*")

@bot.event
async def on_ready():
    print(f"{bot} is ready")


@bot.command()
async def yardım(ctx):
    await ctx.send("nasıl yardımcı olabilirim  bir bilgiyi seçin .atıklar nasıl ayrılır. .geri dönüşüm nedir. .atıklarımız kendimiz nasıl geri dönütürebiliriz.")
@bot.command()
async def geri_dönüşüm_nedir(ctx):
    await ctx.send("https://www.incitas.com.tr/bilgi-merkezi/blog/geri-donusum-nedir-geri-donusumun-faydalari-nelerdir,umarım bu link işinize yarar")
@bot.command()
async def ayrılır_nasıl_ayrılır(ctx):
    await ctx.send("")



bot.run("")
