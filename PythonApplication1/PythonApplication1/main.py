import discord
from discord.ext import commands
from discord.utils import get
import random
import os
import asyncio
from discord import app_commands

bot = commands.Bot(command_prefix="+", intents= discord.Intents.all())
client = commands.Bot(command_prefix="+", intents=discord.Intents.all())
discord_status = "+korhelp"

@client.event
async def on_ready():
    print("Bot is connected to discord")
    await  client.change_presence(activity=discord.Game(discord_status)) 
    synced = await client.tree.sync()
    print(f"Synced {len(synced)} " + "commands.")


@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

@client.tree.command(name= "korhelp")
async def korhelp(interaction: discord.Interaction):
    read_help = "Korcm Bot is a useful discord bot which provides korcm commands.\n\n -> *+korhelp* - Shows all the commands.\n-> *+korandom* - Generates random koray statement.\n-> *+korpick (number)* - Generates a koray statement that you've picked.\n-> *+korembed* - Displays your profile.\n-> *+korpoll* - Poll -Question- -Option1- -Option2-"
    read_help2 = "\n\nAlso you can use */* prefix to use some commands.\n\n->*/korhelp*\n->*/korembed*\n->*/korpick (number)*"
    await interaction.response.send_message(f"Hey {interaction.user.mention}!\n" + read_help + read_help2)

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

@client.tree.command(name= "korpick", description= "Pick a number between 1-520")
async def korpick(interaction: discord.Interaction, number: int): #You need to specify number's type
    with open("d:\\w10\\Desktop\\message.txt", "r") as f:
        line = f.readlines()[int(number) - 1]
        line = line.replace(' ', '-) ', 1)
    await interaction.response.send_message(line)

@client.tree.command(name= "korembed", description= "Tag a user")
async def korembed(interaction: discord.Interaction, avamember: discord.Member = None):
    if avamember == None:
         embed = discord.Embed(description='❌ Error! Please specify a user',
                                  color=discord.Color.red())
         await interaction.response.send_message(embed=embed, mention_author=False)
    else:
         userAvatarUrl = avamember.avatar
         embed = discord.Embed(title=('{}\'s Avatar'.format(avamember.name)), colour=discord.Colour.red())   
         embed.set_image(url='{}'.format(userAvatarUrl))
         await interaction.response.send_message(embed=embed)


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
        await client.start("MTA2ODExOTIwOTIyNzMyOTYwNw.GKUVCk.6iWi_4HfqOx0A9VcOHGGzwEt7r4RIOmJilg-nc")

asyncio.run(main())
