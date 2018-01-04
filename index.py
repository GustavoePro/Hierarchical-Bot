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


"""
@client.event
async def on_message(message):
    #your code starts here:
    if message.content.startswith("#role"):
        team_list = ["R6", "BF1", "CS-GO"]
        entered_team = message.content[6:].lower()
        role = discord.utils.get(message.server.roles, name=entered_team)
        roles = [
        # IDs of the roles for the teams
        "236628751650258944",
        "325076193122451457",
        "326408144693624833",
        ]
    for r in message.author.roles:
        if r.id in roles:
            # If a role in the user's list of roles matches one of those we're checking
            await client.send_message(message.channel, "You already have a/that role. If you want to switch, message a moderator.")
            return
        if role is None or role.name not in team_list:
            # If the role wasn't found by discord.utils.get() or is a role that we don't want to add:
            await client.send_message(message.channel, "The role you requested does not exist, or some error happened.")
            return
        elif role in message.author.roles:
            # If they already have the role
            await client.send_message(message.channel, "You already have this role.")
        else:
            try:
                await client.add_roles(message.author, role)
                await client.send_message(message.channel, "Successfully added role {0}".format(role.name))
            except discord.Forbidden:
                await client.send_message(message.channel, "Lol I can't add roles bro.")
        
    if message.content.upper().startswith("!ADD"):
        args = message.content.split(" ")
        entered_roles = message.content[2:]
        role = discord.utils.get(message.server.roles, name=entered_roles)
        user = discord.utils.find(lambda m: m.name == str(args[1]), message.server.members)
        user_name =  args[1]
        await client.send_message(message.channel, "Now, %s is %s"%(user_name ," ".join(args[2:])))
        await client.add_roles(user, role)

"""

client.run("Mzk2NzU4MTMzMjE4NzM4MTc3.DSq7ug.NzE4Il1OJwUevjRRYTsPeoS7sQE")

