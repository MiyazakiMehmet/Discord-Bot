import discord
from discord.ext import commands
from discord.utils import get
import random
import os
import asyncio

client = commands.Bot(command_prefix="+", intents=discord.Intents.all())
discord_status = "+korhelp"

@client.event
async def on_ready():
    print("Bot is connected to discord")
    await  client.change_presence(activity=discord.Game(discord_status)) 

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

@client.command()
async def korhelp(ctx):
    read_help = "Korcm Bot is a useful discord bot which provides korcm commands.\n\n -> *+korhelp* - Shows all the commands.\n-> *+korandom* - Generates random koray statement.\n-> *+korpick (number)* - Generates a koray statement that you've picked.\n-> *+korembed* - Displays your profile.\n-> *+korpoll* - Poll"
   
    await ctx.send(read_help)

@client.command()
async def korandom(ctx):
    with open("d:\\w10\\Desktop\\message.txt", "r") as f:
        random_response = f.readlines()
        answer = random.choice(random_response) 
        answer = answer.replace(' ', '-) ', 1)
    await ctx.send(answer)

@client.command()
async def korpick(ctx, number):
    with open("d:\\w10\\Desktop\\message.txt", "r") as f:
        line = f.readlines()[int(number) - 1]
        line = line.replace(' ', '-) ', 1)
    await ctx.send(line)

@client.event
async def on_raw_reaction_add(payload):
    if payload.channel_id == 1068190750115909722:
         if payload.emoji.name == "👍":
              channel = client.get_channel(payload.channel_id)
              message = await channel.fetch_message(payload.message_id)
              reaction = get(message.reactions, emoji=payload.emoji.name)
              if reaction and reaction.count >= 5:
                  await message.delete()

async def load():
    for filename in os.listdir("./Cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"Cogs.{filename[:-3]}")

async def main():
    async with client:
        await load()
        await client.start("MTA2ODExOTIwOTIyNzMyOTYwNw.GrZ4IT.vL066vqj_9MOARyNAtBtgkZpNWtsdpURRxBf5Y")

asyncio.run(main())