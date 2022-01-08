import os
try:
    import discord
    import asyncio
    import random 
    import time
    import asyncio
    import wikipedia
except:
    os.system("pip install discord py && pip install wikipedia && pip install asyncio")
    
from random import choice, randint
from discord.ext import tasks, commands

settings = {
    "prefix": "//",
    "token": "token"
}

client = commands.Bot(command_prefix = settings["prefix"], self_bot = True, help_command=None)

#config
color = discord.Colour.from_rgb(0, 0, 0) # color in rgb format''

@client.event
async def on_ready():
	print('Loggined in as {0.user}'.format(client))
	await client.change_presence(status=discord.Status.idle,activity=discord.Game("DenzBox | 0.2"))

@client.event
async def on_command_error( ctx, error ):
	if isinstance( error, commands.CommandNotFound ):
	    await ctx.send("Invalid command")
	    print("[log] Error: Invalid command")
	elif isinstance( error, commands.MissingRequiredArgument ):
	    await ctx.send("Missing required argument")
	    print("[log] Error: Missing required argument")
	else:
	    await ctx.send("Something went wrong")
	    print("[log] Error: Something went wrong")
	
@client.command()
async def help(ctx):
	desc = "```info``` - Shows information\n```embed {message}``` - Sends an embed message\n```game {status}``` - Sets the status playing a game\n```listen {status}``` - Sets the status listening to\n```kick @Member {reason}``` - Kick a member\n```ban @Member {reason}``` - kick the member\n```nickname @Member {nickname}``` - Changes nickname to a member\n```spam {quantity} {delay} {message}``` - Spamming with a message\n```calc {expression}``` - Simple calculator\n```clear {number}``` - Clears chat messages\n```suicide``` Make suicide\n```wiki {search query}``` - Searches wiki page\n```random {first number} {second number}``` - random number\n```tspam {count} {text}``` - Spam with text channels\n```vspam {count} {text}``` - Spam with voice channels\n```srvname {name}``` - Changes the server name"	
	embed = discord.Embed(title='Help', description=desc, color=color)
	await ctx.send(embed=embed)
	print('[log] Command help')
	
@client.command()
async def info(ctx):
	embed = discord.Embed(title='Info', description=f"Ping = {round(client.latency * 1000)}ms\ncolor = {color}", color=color)
	await ctx.send(embed=embed)
	print('[log] Command info')
	
@client.command(aliases = ["emb"])
async def embed(ctx, *, text):
	embed = discord.Embed(description=text, color=color)
	await ctx.send(embed=embed)
	await ctx.message.delete()
	print('[log] Command embed')
	
@client.command()
async def game(ctx, *, text):
	await client.change_presence(status=discord.Status.idle,activity=discord.Game(text))
	embed = discord.Embed(title='Change status', description=f"Now the status: {text}", color=color)
	await ctx.send(embed=embed)
	print(f"[log] Now the status {text}")
	print('[log] Command game')
	
@client.command()
async def listen(ctx, *, text):
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=text))
	embed = discord.Embed(title='Change status', description=f"Now the status: {text}", color=color)
	await ctx.send(embed=embed)
	print(f"[log] Now the status {text}")
	print('[log] Command listen')
	
@client.command()
async def calc(ctx, *, text):
	evl = eval(text)
	embed = discord.Embed(title='Calc', description=f"{text} = {evl}", color=color)
	await ctx.send(embed=embed)
	print('[log] Command calc')
	
	
@client.command()
async def kick(ctx, member: discord.Member, *, reason):
	await ctx.guild.kick(member, reason=reason)
	embed = discord.Embed(title="Kick", description=f"Member {member} was kicked\nReason: {reason}", color=color)
	await ctx.send(embed=embed)
	print('[log] Command kick')
	
@client.command()
async def ban(ctx, member: discord.Member, *, reason = None):
	await ctx.guild.ban(member, reason=reason)
	embed = discord.Embed(title="Ban", description=f"Member {member} was banned\nReason: {reason}", color=color)
	await ctx.send(embed=embed)
	print('[log] Command ban')
	
@client.command()
async def banid(ctx, member: str, *, reason = None):
	await ctx.guild.ban(member, reason=reason)
	embed = discord.Embed(title="BanID", description=f"Member {member} was banned\nReason: {reason}", color=color)
	await ctx.send(embed=embed)
	print('[log] Command banid')
	
@client.command(aliases = ["nick"])
async def nickname(ctx, member: discord.Member, *, nick):
	await member.edit(nick=nick)
	embed = discord.Embed(title='Nickname', description=f"Now the user {member} has nickname {nick}", color=color)
	await ctx.send(embed=embed)
	print('[log] Command nickname')
		
@client.command()
async def spam(ctx, count: int, delay: float, *, text):
	 	 print('[log] Command spam')
	 	 for i in range(int(count)):
	 	 	await ctx.send(text)
	 	 	await asyncio.sleep(float(delay))
	 	 	
@client.command()
async def image(ctx, url):
	embed = discord.Embed(description='hm', image=url)
	await ctx.send(embed=embed)
	
@client.command()
async def clear(ctx, count: int):
	print('[log] Command clear')
	await ctx.channel.purge(limit=int(count))
	
@client.command()
async def suicide(ctx):
	 	 print('[log] Command suicide')
	 	 message = await ctx.send(':smiling_face_with_tear: :gun:')
	 	 await asyncio.sleep(1)
	 	 await message.edit(content=':boom:')
	 	 await asyncio.sleep(1)
	 	 await message.edit(content=':skull:')
	 	 
@client.command()
async def wiki(ctx, *, sr):
	print('[log] Command wiki')
	index = wikipedia.page(sr)
	result = wikipedia.summary(sr)
	title = index.title
	url = index.url
	embed = discord.Embed(title=f"Wikipedia: {title}",description=f"{result}", color=color, url=url)
	await ctx.send(embed=embed)
	
@client.command(aliases = ["rand"])
async def random(ctx, o: int, t: int):
	print("[log] Command random")
	random = randint(int(o),int(t))
	embed = discord.Embed(title='Random', description=random, color=color)
	await ctx.send(embed=embed)
	
@client.command()
async def tspam(ctx, count, *, text):
	print('[log] Command tspam')
	for i in range(int(count)):
		guild = ctx.message.guild
		await guild.create_text_channel(text)
		
@client.command()
async def vspam(ctx, count, *, text):
	print('[log] Command v spam')
	for i in range(int(count)):
		guild = ctx.message.guild
		await guild.create_voice_channel(text)

@client.command()
async def srvname(ctx, *, name):
	print('[log] Command srvname')
	await ctx.guild.edit(name=name)
	embed = discord.Embed(title="Server name", description=f"now the server name is {name}", color=color)
	await ctx.send(embed=embed)
	
client.run(settings["token"], bot = False)  