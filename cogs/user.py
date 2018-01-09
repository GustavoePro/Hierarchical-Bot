#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
import asyncio

class User():
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, description="add specified roles to a specified user")
    async def add(self, ctx, userParameter : str, *rolesParameter : str): 
        # Defini um objeto "discord.members"(user) e verifica sua existência:
        user = discord.utils.get(ctx.message.server.members, name=userParameter)
        if user is None:
            await self.client.say('The user " **%s** " does not exist'%(userParameter))
            return
        # Defini uma lista com os objetos "discord.roles"(roles) e verifica suas condições:
        roles = []
        for r in rolesParameter:
            utils_get = discord.utils.get(user.server.roles, name=r)
            if utils_get is None:
                await self.client.say('The role " **%s** " does not exist.'%(r))
            elif utils_get in user.roles:
                await self.client.say('The user **%s** already has the role **%s**.'%(user.name,r))
            else:
                roles.append(utils_get)
        # Adiciona as roles ao user, caso possível:
        str_roles = [a.name for a in roles]
        try:
            await self.client.add_roles(user, *roles)
            if len(str_roles) == 1:
                await self.client.say("Now, <@%s> has the role **%s**!"%(user.id, str_roles[0]))
            elif len(str_roles) == 2:
                await self.client.say("Now, <@%s> has the role **%s** and **%s**!"%(user.id, str_roles[0],str_roles[1]))
            elif len(str_roles) > 2:
                await self.client.say("Now, <@%s> has the role **%s**, **%s** and **%s**!"%(user.id, str_roles[0],
                ", ".join(str_roles[1:-1]), str_roles[-1]))
        except Exception:
            await self.client.say("You do not have permission.")
            return
        
    @commands.command(pass_context=True)
    async def remove(ctx, userParameter : str, *rolesParameter : str):
        # Defini um objeto "discord.members"(user) e verifica sua existência:
        user = discord.utils.get(ctx.message.server.members, name=userParameter)
        if user is None:
            await self.client.say('The user " **%s** " does not exist.'%(userParameter))
            return
        # Defini uma lista com os objetos "discord.roles"(roles) e verifica suas condições:
        roles = []
        for r in rolesParameter:    
            utils_get = discord.utils.get(user.server.roles, name=r)
            if utils_get not in user.roles:
                await self.client.say('The user **%s** does not have the role **%s**.'%(user.name,r))
            else:
                roles.append(utils_get)
        # Remove as roles ao user, caso possível:
        str_roles = [a.name for a in roles]
        try:
            await self.client.remove_roles(user, *roles)
            if len(str_roles) == 1:
                await self.client.say("Now, <@%s> no longer has the role **%s**!"%(user.id, str_roles[0]))
            elif len(str_roles) == 2:
                await self.client.say("Now, <@%s> no longer has the role **%s** and **%s**!"%(user.id, str_roles[0],str_roles[1]))
            elif len(str_roles) > 2:
                await self.client.say("Now, <@%s> no longer has the role **%s**, **%s** and **%s**!"%(user.id, str_roles[0],
                ", ".join(str_roles[1:-1]), str_roles[-1]))
        except Exception:
            await self.client.say("You do not have permission.")
            return

def setup(client):
    client.add_cog(User(client))
