import discord
from discord.ext import commands
from discord.utils import get

bot = discord.ext.commands.Bot(command_prefix = "+", intents=discord.Intents.all());

class MyCog(commands.Cog):
    def __init__(self, client):
        self.client = client


    #Displaying Profile Picture
    @commands.command()
    async def korembed(self, ctx, *, avamember: discord.Member = None):
        if avamember == None:
            embed = discord.Embed(description='❌ Error! Please specify a user',
                                  color=discord.Color.red())
            await ctx.reply(embed=embed, mention_author=False)
        else:
            userAvatarUrl = avamember.avatar
            if(ctx.message.mentions[0].id == 206003447655432192): #Checks id of the person who tagged
                embed = discord.Embed(title="GORAY GURT's Avatar", colour=discord.Colour.red())
            else:
                embed = discord.Embed(title=('{}\'s Avatar'.format(avamember.name)), colour=discord.Colour.red())   
            embed.set_image(url='{}'.format(userAvatarUrl))
            await ctx.reply(embed=embed, mention_author=False) 

    #Kicks the user
    @bot.command(pass_context=True)
    async def korkick(self, ctx, user: discord.Member):
        #if(ctx.message.mentions[0].id == 206003447655432192): #Checks id of the person who tagged
        await ctx.guild.kick(user)

    #Poll
    @commands.has_permissions(manage_messages=True)
    @commands.command(pass_context=True)
    async def korpoll(self, ctx, question, *options: str):

        if len(options) > 2:
            embed = discord.Embed(description='❌ "Question", "Option1", "Option2"',
                                  color=discord.Color.red())
            await ctx.reply(embed=embed, mention_author=False)
            return
        elif len(options) < 2 or len(options) == 0:
            embed = discord.Embed(description='❌ Please specify 3 options ',
                                  color=discord.Color.red())
            await ctx.reply(embed=embed, mention_author=False)
            return
        if len(options) == 2 and options[0] == "yes" and options[1] == "no":
            reactions = ['👍', '👎']
        else:
            reactions = ['👍', '👎']

        description = []
        for x, option in enumerate(options):
            description += '\n\n {} {}'.format(reactions[x], option)

        poll_embed = discord.Embed(title=question, color=0x31FF00, description=''.join(description))

        react_message = await ctx.send(embed=poll_embed)

        for reaction in reactions[:len(options)]:
            await react_message.add_reaction(reaction)


async def setup(client):
    await client.add_cog(MyCog(client))
