import discord, io
import time
from io import BytesIO
import json
import requests
from discord.ext import commands
import socket
import struct
import codecs,sys
import threading
import random
import os

    
intents = discord.Intents().all()
bot = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="t!",intents=intents)


@bot.command()
async def ddos(ctx, ip, port):
  await ctx.send(f"Ddos attack to {ip}:{port}")
  os.system(f"python ddos.py {ip} {port}")
  exit()
  
  

@bot.command(name="proxy")
@commands.cooldown(1, 10, commands.BucketType.user)
async def proxy(ctx, *, args = None):
    if args is None:
      await ctx.send("""
      ```
Usage $proxy <type>
example $proxy http
Type:
 http
 socks4
 socks5
       ```
       """)
    else:
      if args == "http":
        await ctx.send("Downloading proxies...")
        proxy = "https://api.proxyscrape.com/?request=displayproxies&proxytype=http"
        url = requests.get(proxy,timeout=5).text
        data = BytesIO(url.encode("utf-8"))
        await ctx.send(content=f"**Succes download proxy {args}!**",file=discord.File(data,filename=f"{args}"))
      elif args == "socks4":
        await ctx.send("Downloading proxies...")
        proxy = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4"
        url = requests.get(proxy,timeout=5).text
        data = BytesIO(url.encode("utf-8"))
        await ctx.send(content=f"**Succes download proxy {args}!**",file=discord.File(data,filename=f"{args}"))
      elif args == "socks5":
        await ctx.send("Downloading proxies...")
        proxy = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true"
        url = requests.get(proxy,timeout=5).text
        data = BytesIO(url.encode("utf-8"))
        await ctx.send(content=f"**Succes download proxy {args}!**",file=discord.File(data,filename=f"{args}"))
      else:
        await ctx.send("Not Found proxies..")



@bot.event
async def on_ready():
    activity = discord.Game(name="Testi Bot", type=3)
    await bot.change_presence(status=discord.Status.invisible, activity=activity)
    print (bot.user.name + " Is Online!")

bot.run("")
