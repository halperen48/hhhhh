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
    await ctx.send("nasıl yardımcı olabilirim  bir bilgiyi seçin .atıklar nasıl ayrılır. .geri_dönüşüm_nedir. .atıklarımız_kendimiz_nasıl_geri_dönütürebiliriz.")

@bot.command()
async def geri_dönüşüm_nedir(ctx):
    await ctx.send("https://www.incitas.com.tr/bilgi-merkezi/blog/geri-donusum-nedir-geri-donusumun-faydalari-nelerdir")

@bot.command()
async def atıklar_nasıl_ayrılır(ctx):
    await ctx.send("atıklar cam metal plastik ve kağıt olarak ayrılır ayrıca atıklar organik evsel atıklar, geri dönüştürülebilir evsel atıklar, tehlikeli evsel atıklar olarak guruplandırılır")

@bot.command()
async def atıklarımız_kendimiz_nasıl_geri_dönütürebiliriz(ctx):
    await ctx.send("atık seçin .cam. .kağıt. .metal. .plastik.")

@bot.command()
async def cam(ctx):
    await ctx.send("http://www.ozencam.com.tr/Faaliyetler/157-cam-atiklar-ve-geri-donusum.aspx#:~:text=%100%20oran%C4%B1nda%20geri%20d%C3%B6n%C3%BC%C5%9Fl%C3%BC%20olan,sodadan%20daha%20d%C3%BC%C5%9F%C3%BCk%20s%C4%B1cakl%C4%B1kta%20erir.")

@bot.command()
async def kağıt(ctx):
    await ctx.send("https://www.haypak.com.tr/blogs/haypak/turkiye-de-kagit-geri-donusumu#:~:text=At%C4%B1k%20ka%C4%9F%C4%B1tlar%2C%20ka%C4%9F%C4%B1t%20geri%20d%C3%B6n%C3%BC%C5%9F%C3%BCm,ka%C4%9F%C4%B1t%20geri%20d%C3%B6n%C3%BC%C5%9F%C3%BCm%20tesisine%20ta%C5%9F%C4%B1n%C4%B1r.")

@bot.command()
async def plastik(ctx):
    await ctx.send("plastik konusunu önemi ve araştırmasındaki genişlilikten dolayı googledan bakmanızı öneririm ")
    await ctx.send("https://www.google.com/search?q=plasti%C4%9Fin+geri+d%C3%B6n%C3%BC%C5%9F%C3%BCm%C3%BC&sca_esv=567866750&bih=739&biw=1536&hl=tr&sxsrf=AM9HkKmhmNLrFK1uVEF7Fhk1im4IzY-ZZQ%3A1695484457331&ei=KQoPZbjmE8a-xc8PjuyTwAE&ved=0ahUKEwj4nrTmi8GBAxVGX_EDHQ72BBgQ4dUDCBA&uact=5&oq=plasti%C4%9Fin+geri+d%C3%B6n%C3%BC%C5%9F%C3%BCm%C3%BC&gs_lp=Egxnd3Mtd2l6LXNlcnAiHXBsYXN0acSfaW4gZ2VyaSBkw7Zuw7zFn8O8bcO8MgUQABiABDIFEAAYgAQyBRAAGIAEMgQQABgeSPNMUP0IWIc1cAF4AZABAJgBkgGgAa4OqgEEMC4xNLgBA8gBAPgBAcICChAAGEcY1gQYsAPCAgoQABiKBRiwAxhDwgIHECMYsAIYJ8ICBxAAGA0YgATCAgYQABgHGB7CAgcQABiKBRhDwgIIEAAYBxgeGA_iAwQYACBBiAYBkAYK&sclient=gws-wiz-serp")
@bot.command()
async def metal(ctx):
    await ctx.send("https://www.cevremuhendisligi.org/index.php/sifir-atik/1104-metal-atiklarin-geri-kazanimi")


bot.run("")
