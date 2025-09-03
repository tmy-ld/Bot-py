import discord
from discord.ext import commands
import os, random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix= "!", intents=intents)

@bot.event
async def on_ready():
    print(f"Hemos iniciado secion como {bot.user}")

@bot.command()
async def mem(ctx, tema):
    if tema == "general":
        img_name = random.choice(os.listdir("Meme"))
        with open(f'Meme/{img_name}', 'rb') as f:
            picture = discord.File(f)ñ
        await ctx.send(file=picture)
    elif tema == "gato":
        img_name = random.choice(os.listdir("Meme 2"))
        with open(f'Meme 2/{img_name}', 'rb') as f:
            picture = discord.File(f)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("ñ")
