import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

# --- كود التشغيل المستمر ---
app = Flask('')

@app.route('/')
def home():
    return "I'm Alive"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
# -------------------------

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def promo(ctx):
    try:
        await ctx.message.delete()
    except:
        pass
    content = (
        "**تم توفير نيتـ؛روهات قيـ؛فت ( شهر )**\n"
        "** بـ  18,5 ريال  <:70226nitrostylediamond:1461906861497516115>  **\n\n"
        "للطلب او للإستفسار : [اضغط هنا](https://discord.com/channels/1455993144645648517/1456000073208037427)\n"
        "لقراءة الشروط والاحكام : [اضغط هنا](https://discord.com/channels/1455993144645648517/1455999275325460502)\n"
        "-# عند شراءك فـ أنت توافق على الشروط ، تقولي ماقريت مب عذر\n"
        "** @everyone **"
    )
    await ctx.send(content)

keep_alive()
bot.run('MTQ2NTMzMzg5MTk3MDc2MDkwMwGl2kmH0scyz6A_iipqrmPTIv4ZgEps8jnXQHXxQOLIlo')
