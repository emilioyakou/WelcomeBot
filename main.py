import discord
import datetime
from discord.ext import commands

welcome_channel = 1120206504616804432 #Variable for Channel ID

bot = commands.Bot(command_prefix='.', intents=discord.Intents.default())


@bot.event
async def on_ready():
    print("Bot is Online")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(welcome_channel)
    embed = discord.Embed(
        description=f'Welcome **{member.mention}** to the server.',   #Message when someone joins ** = bold
        timestamp=datetime.datetime.now()
    )
    role = discord.utils.get(member.guild.roles, name="Member")
    await member.add_roles(role)
    await channel.send(embed=embed)


bot.run("MTEyMDIwMzExNTAwMjYwMTU2NQ.Gmbxlx.wkwGS3ft5AJbxComeVzsLN5PvaCaoceS-YsEy8")