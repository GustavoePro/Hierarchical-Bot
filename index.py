import discord
from discord.ext import commands
import asyncio
import time
import random
from discord.ext.commands import errors
import sys


description = '''lol'''

Client = discord.Client()
client = commands.Bot(command_prefix = "!")
initial_extensions = ["cogs.exec"]

        
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


@client.command(pass_context=True)
async def role_stats(ctx, role_name : str):
    # Comando ainda em teste
    role = discord.utils.get(ctx.message.server.roles, name=role_name)
    embed=discord.Embed(title="Role: %s"%(role.name), description="Desc", colour=int("0x0066ff", 16))
    embed.add_field(name="Fiel1", value="hi", inline=False)
    embed.add_field(name="Field2", value="hi2", inline=False)
    await client.say(embed=embed)
    role.permissions.kick_members = True
    await client.edit_role(ctx.message.server, role, permissions = role.permissions)
    await client.say(role.permissions.kick_members)

if __name__ == "__main__":
    for extension in initial_extensions:
        try:
            client.load_extension(extension)
            print('Extension {} loaded.'.format(extension))
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
    
    client.run("Mzk2NzU4MTMzMjE4NzM4MTc3.DSq7ug.NzE4Il1OJwUevjRRYTsPeoS7sQE")
