#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
import asyncio
from colour import Color

class Roles():
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

    @commands.command(pass_context=True)
    async def create(self, ctx, role_name : str, color : str):
        # Testa se as entradas do usuário existe:
        if role_name == None:
            await self.client.say("The role's name is required to create the role.")
            return
        # Cria a role com o nome e a cor especificada, se possivel:
        try:
            await self.client.create_role(ctx.message.server, name=role_name, colour=discord.Colour(int(Color(color).hex_l.replace("#", "0x"), 16)))
            await self.client.say("The role **%s** has been created."%(role_name))
        except ValueError:
            await self.client.say("The role color must be a color name or a hexadecimal number(ex:#0088ff).")
            return
        except discord.Forbidden:
            await self.client.say("You do not have permission.")
            return

    @commands.command(pass_context=True)
    async def delete(self, ctx, role_name : str):
        # Defini um objeto "discord.role" e verifica sua existência:
        role = discord.utils.get(ctx.message.server.roles, name=role_name)
        if role_name == None:
            await self.client.say("The role's name is required to delete the role.")
            return
        # Deleta a role do servidor, se possível:
        try:
            await self.client.delete_role(ctx.message.server, role)
            await self.client.say("The role **%s** has been deleted."%(role_name))
        except AttributeError:
            await self.client.say("The role **%s** does not exist."%(role_name))
        except discord.Forbidden:
            await self.client.say("You do not have permission.")
    
    @commands.command(pass_context=True)
    async def edit(self, ctx, role_name : str, role_att : str, att_value : str):
        # Verifica se os parâmetros foram concedidos:
        if role_name == None:
            await self.client.say("The role's name is required to edit the role.")
            return
        if role_att == None:
            await self.client.say("The role attribute name is required to edit the role.")
            return
        if att_value == None:
            await self.client.say("The attribute value is required to edit the role.")
            return
        # Defini o objeto "discord.role":
        role = discord.utils.get(ctx.message.server.roles, name=role_name)
        att_value = att_value.lower()
        role_att = role_att.lower()
        # Testa o parâmetro "role_att" e o muda de acordo com o parâmetro "att_value":
        if role_att == "colour" or role_att == "color":
            try:
                await self.client.edit_role(ctx.message.server, role, colour = discord.Colour(int(Color(att_value).hex_l.replace("#", "0x"), 16)))
                await self.client.say("The role **%s** had the color changed for **%s**."%(role.name, att_value))
                return
            except ValueError:
                await self.client.say("The role color must be a color name or a hexadecimal number(ex:#0088ff).")
                return
            except discord.Forbidden:
                await self.client.say("You do not have permission.")
                return
        elif att_value != "false" or att_value != "true":
            await self.client.say("The attribute value %s does not exist."%(att_value))
            return
        elif role_att == "create_instant_invite":
            if att_value == "true":
                role.permissions.create_instant_invite = True
                await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
                return
            elif att_value == "false" or att_value == "false":
                role.permissions.create_instant_invite = False
                await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
                return
        return

def setup(client):
    client.add_cog(Roles(client))
