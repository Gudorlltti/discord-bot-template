import nextcord
from nextcord.ext import commands
import time, sys, datetime, os, random, json
import asyncio, aiohttp

intents = nextcord.Intents.all()

prefix = "!"
client = commands.Bot(command_prefix=prefix,intents=intents)

#client.remove_command("help")

token = "YOUR SUPER SECRET BOT TOKEN"

async def status_task():
    while True:
        await client.change_presence(status=nextcord.Status.online,activity=nextcord.Game(f"{prefix}help")) 
        await asyncio.sleep(5)
        await client.change_presence(status=nextcord.Status.online,activity=nextcord.Game(f"on {len(client.guilds)} servers!")) 
        await asyncio.sleep(5)
        

@client.event
async def on_ready():
    print(f"Sucessfully logged in as {client.user}")    
    await client.change_presence(status=nextcord.Status.online,activity=nextcord.Game("Bot is ready!"))
    await asyncio.sleep(2)
    client.loop.create_task(status_task())
    
    
@client.command()
async def ping(ctx): 
    await ctx.send(f'Pong! {round (client.latency * 1000)} ms')
    
@client.command()
async def invite(ctx):
    await ctx.reply(f"https://discord.com/api/oauth2/authorize?client_id={client.id}&permissions=8&scope=bot%20applications.commands")

    
@client.command()
@commands.is_owner()
async def load(ctx, e):
    client.load_extension(f"cogs{e}")
    await ctx.reply(f"Loaded {e}!")
    
@client.command()
@commands.is_owner()
async def unload(ctx, e):
    client.unload_extension(f"cogs{e}")
    await ctx.reply(f"Unloaded {e}!")

@client.command()
@commands.is_owner()
async def reload(ctx, e):
    client.reload_extension(f"cogs{e}")
    await ctx.reply(f"Reloaded {e}!")
    
    
    
 for f in os.listdir("./cogs"):
	if f.endswith(".py"):
		client.load_extension("cogs." + f[:-3])
    
client.run(token)
