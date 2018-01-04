import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    if message.content.upper().startswith("!PING"):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!"%(userID))
    if message.content.upper().startswith("!SAY"):
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" %(" ".join(args[1:])))
    await client.process_commands(message)

@client.command()
async def add(user : discord.Member, *roles: discord.Role):
    await client.say("oi")
    return
    str_roles = [a.name for a in roles]
    for r in roles:
        if r not in user.server.roles:
            await client.say("This role %s do not exist."%(r.name))
    try:
        await client.add_roles(user, *roles)
        if len(str_roles) == 1:
            await client.say("Now, <@%s> has the role %s!"%(user.id, str_roles[0]))
        elif len(str_roles) == 2:
            await client.say("Now, <@%s> has the role %s and %s!"%(user.id, str_roles[0],str_roles[1]))
        elif len(str_roles) > 2:
            await client.say("Now, <@%s> has the role %s, %s and %s!"%(user.id, str_roles[0], ", ".join(str_roles[1:-1]), str_roles[-1]))
    except Exception:
        await client.say("You do not have permission")
        return

client.run("Mzk2NzU4MTMzMjE4NzM4MTc3.DSq7ug.NzE4Il1OJwUevjRRYTsPeoS7sQE")
