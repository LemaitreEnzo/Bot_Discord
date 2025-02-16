import discord
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    print("Le bot est prêt !")

@client.event
async def on_message(message):
    if message.content == "Ping":
        await message.channel.send("Pong")



@client.event
async def on_member_join(member):
    general_channel = client.get_channel(1168637682595922056)
    general_channel.send(f"Bienvenue sur le serveur {member.display_name} !")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def salut(ctx):
    await ctx.send('Bonjour !')

client.run('VOTRE_TOKEN_ICI')