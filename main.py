import asyncio
import os

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())
bot.remove_command("help")


@bot.event
async def on_ready():
    print("Ich bin jetzt online")


async def status_task():
    while True:
        await bot.change_presence(status=discord.Status.online, activity=discord.Game
        ("?help"))
        await asyncio.sleep(10)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game
        (f"{len(set(bot.users))} Member"))
        await asyncio.sleep(10)

for filename in os .listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


@bot.command()
async def test(ctx):
    await ctx.send("Bestanden")


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member = None, *, reason=None):
    if member is None:
        await ctx.send("Es ist kein user angegeben")
        return
    elif reason is None:
        await ctx.send(f"Du solltest noch eine Begründung angeben um den User {member.mention} zu kicken")
        return
    embed = discord.Embed(title="Erfolgreich gekickt", description=f"Ich habe für dich {member.mention} gekickt",
                          color=discord.Colour.blurple())
    await ctx.send(embed=embed)
    await member.kick(reason=reason)


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member = None, *, reason=None):
    if member is None:
        await ctx.send("Es ist kein user angegeben")
        return
    elif reason is None:
        await ctx.send(f"Du solltest noch eine Begründung angeben um den User {member.mention} zu bannen")
        return
    embed = discord.Embed(title="Erfolgreich gebannt", description=f"Ich habe für dich {member.mention} gebannt",
                          color=discord.Colour.random())
    await ctx.send(embed=embed)
    await member.ban(reason=reason)


@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    if member:
        embed = discord.Embed(title=f"Userinfo für {member.display_name}", color=0xff0000)
        embed.add_field(name="Name", value=f"```{member}```")
        embed.add_field(name="Status:", value=f"```{member.status}```")
        embed.add_field(name="Bot:", value=f'```{("Ja" if member.bot else "Nein")}```')
        embed.add_field(name="Server beigetreten:", value=f"```{member.joined_at}```")
        embed.add_field(name="Discord beigetreten:", value=f"```{member.created_at}```")
        embed.add_field(name="Rollen:", value=f"```{len(member.roles) - 1}```")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title=f"Userinfo für {ctx.author.display_name}", color=0xff0000)
        embed.add_field(name="Name", value=f"```{ctx.author}```")
        embed.add_field(name="Status:", value=f"```{ctx.author.status}```")
        embed.add_field(name="Bot:", value=f'```{("Yes" if ctx.author.bot else "no")}```')
        embed.add_field(name="Server beigetreten:", value=f"```{ctx.author.joined_at}```")
        embed.add_field(name="Discord beigetreten:", value=f"```{ctx.author.created_at}```")
        embed.add_field(name="Rollen:", value=f"```{len(ctx.author.roles) - 1}```")
        await ctx.send(embed=embed)


@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong:ping_pong:  **{round(bot.latency * 1000)}ms**")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(940656317201264663)
    embed = discord.Embed(title="👋    | Wilkommen auf diesem Server",
                          description=f"Herzlich Willkommen {member.mention} Bitte akzeptiere das Regelwerk")
    embed.add_field(name="Wir freuen uns dich zu sehen",
                    value=f" Wir sind jetzt {len(set(bot.users))} auf diesem Server")
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/883805723807588423/901580387950686259/zerotwo_ist_scheie.gif")
    await channel.send(embed=embed)


bot.run("OTQyMDA0ODM0OTMwOTE3NDY3.YgeMXg.ANBimedBgc5K6Iy1Q3mek_Sx4iA")
