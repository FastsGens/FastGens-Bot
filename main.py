import discord
import os
import asyncio
import aiohttp
import json
from discord.ext import commands
from discord import File
import string
import io
import math
import requests
client = commands.Bot(command_prefix='.',case_insensitive=True)
TOKEN=('yourtoken')

client.remove_command('help')


@client.event
async def on_member_join(ctx, *, member):
    channel = ctx.guild.get_channel(836699680959234048)
    embed2 = discord.Embed(title=f"Welcome to FastGens",
                      description=f"{ctx.author.mention}")
    
    message = await channel.send(embed=embed2)
    await message.add_reaction('\U0001f7e2')


@client.command(name='generate')
@commands.has_any_role('[Customer]')
@commands.cooldown(1, 10, commands.BucketType.user)
async def generate(ctx, arg1):
     async with aiohttp.ClientSession() as session:
        async with session.get(f'https://fastgens.com/api/generate.php?user=yourpass&type={arg1}') as resp:
            await ctx.send(await resp.text())


@client.command(name='suggest')
@commands.cooldown(1, 10, commands.BucketType.user)
async def suggest(ctx,*,arg1):
    channel = ctx.guild.get_channel(836381209227296788)
    embed = discord.Embed(title=f"New Suggestion",
                      description=f"{arg1}\n\n Suggested by {ctx.author.mention}")
    
    message = await channel.send(embed=embed)
    await message.add_reaction('\U0001f7e2')
    await message.add_reaction('\U0001f534')


@client.command(name='report')
@commands.cooldown(1, 10, commands.BucketType.user)
async def report(ctx,*,arg1):
    channel = ctx.guild.get_channel(836693892573036565)
    embed = discord.Embed(title=f"New Report",
                      description=f"{arg1}\n\n Reported by {ctx.author.mention}")
    
    message = await channel.send(embed=embed)
    await message.add_reaction('\U0001f7e2')
    await message.add_reaction('\U0001f534')

@client.command(name='help')
async def help(ctx):
    embed1 = discord.Embed(title="FastGens Help",
                      description=".report - report a user for scamming or other things\n.suggest - make a suggestions\n\nPremium\n\n.generate accounttype")
    
    
    await message.ctx.send(embed=embed1)
    
#DO NOT DELETE:
#           "6f/77/6e/65/64/20/62/79/20/70/68/61/6e/74/6f/6d/20/73/65/72/76/69/63/65/73/2e"

async def role(ctx, member: discord.Member):
    await member.add_roles('[Customer]')
    await ctx.send(f"{discord.Member.mention} is now a customer!")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        embed = discord.Embed(title="Please provide an account type, this one seems to be invaild",color=discord.Color.from_rgb(255, 0, 0))
        await ctx.send(embed=embed)
    if isinstance(error, commands.errors.MissingAnyRole):
        embed = discord.Embed(title="Please contact the owner to purchase a plan to gain access to this command!",color=discord.Color.from_rgb(255, 0, 0))
        await ctx.send(embed=embed)
    if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("This command is on cooldown, please retry in {}s.".format(math.ceil(error.retry_after)))
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title="you need to be a admin to do this!",color=discord.Color.from_rgb(255, 0, 0))
        await ctx.send(embed=embed)
        

client.run(TOKEN)
