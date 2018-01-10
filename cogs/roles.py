#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
import asyncio
from colour import Color

class Roles():
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def create(self, ctx, role_name : str, color : str = "#99AAB5"):
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
    async def edit(self, ctx, role_name : str, role_att : str, att_value : str = "undefined"):
        # Verifica se os parâmetros foram concedidos:
        role = discord.utils.get(ctx.message.server.roles, name=role_name)
        if role_name == None or role == None:
            await self.client.say("The role's name is required to edit the role.")
            return
        if role_att == None:
            await self.client.say("The role attribute name is required to edit the role.")
            return
        role = discord.utils.get(ctx.message.server.roles, name=role_name)
        role_att = role_att.lower()
        # Testa o parâmetro "role_att" e o muda de acordo com o parâmetro "att_value":
        if role_att == "colour" or role_att == "color":
            try:
                await self.client.edit_role(ctx.message.server, role, colour = discord.Colour(int(Color(att_value).hex_l.replace("#", "0x"), 16)))
                await self.client.say("The role **%s** had the color changed for **%s**."%(role.name, att_value.lower()))
                return
            except ValueError:
                await self.client.say("The role color must be a color name or a hexadecimal number(ex:#0088ff).")
                return
            except discord.Forbidden:
                await self.client.say("You do not have permission.")
                return
        if role_att == "name":
            try:
                await self.client.edit_role(ctx.message.server, role, name=att_value)
            except Exception:
                await self.client.say("You do not have permission.")
        att_value = att_value.lower()
        try:
            if att_value != "false" and att_value != "true" and att_value != "undefined":
                await self.client.say("The attribute value **%s** does not exist."%(att_value))
                return
            elif role_att == "create_instant_invite": # 1 
                if att_value == "true":
                    role.permissions.create_instant_invite = True
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
                elif att_value == "false":
                    role.permissions.create_instant_invite = False
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
            elif role_att == "kick_members": # 2
                if att_value == "true":
                    role.permissions.kick_members = True
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
                elif att_value == "false":
                    role.permissions.kick_members = False
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
            elif role_att == "ban_members": # 3
                if att_value == "true":
                    role.permissions.ban_members = True
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
                elif att_value == "false":
                    role.permissions.ban_members = False
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
            elif role_att == "administrator": # 4
                if att_value == "true":
                    role.permissions.administrator = True
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
                elif att_value == "false":
                    role.permissions.administrator = False
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
            elif role_att == "manage_channels": # 5
                if att_value == "true":
                    role.permissions.manage_channels = True
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
                elif att_value == "false":
                    role.permissions.manage_channels = False
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
            elif role_att == "manage_server": # 6
                if att_value == "true":
                    role.permissions.manage_server = True
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
                elif att_value == "false":
                    role.permissions.manage_server = False
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
            elif role_att == "add_reactions": # 7
                if att_value == "true":
                    role.permissions.add_reactions = True
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
                elif att_value == "false":
                    role.permissions.add_reactions = False
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
            elif role_att == "view_audit_logs": # 8
                if att_value == "true":
                    role.permissions.view_audit_logs = True
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
                elif att_value == "false":
                    role.permissions.view_audit_logs = False
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
            elif role_att == "read_messages": # 9
                if att_value == "true":
                    role.permissions.read_messages = True
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
                elif att_value == "false":
                    role.permissions.read_messages = False
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
            elif role_att == "send_messages": # 10
                if att_value == "true":
                    role.permissions.send_messages = True
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
                elif att_value == "false":
                    role.permissions.send_messages = False
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
            elif role_att == "send_tts_messages": # 11
                if att_value == "true":
                    role.permissions.send_tts_messages = True
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
                elif att_value == "false":
                    role.permissions.send_tts_messages = False
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
            elif role_att == "manage_messages": # 12
                if att_value == "true":
                    role.permissions.manage_messages = True
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
                elif att_value == "false":
                    role.permissions.manage_messages = False
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
            elif role_att == "embed_links": # 13
                if att_value == "true":
                    role.permissions.embed_links = True
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
                elif att_value == "false":
                    role.permissions.embed_links = False
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
            elif role_att == "attach_files": # 14
                if att_value == "true":
                    role.permissions.attach_files = True
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
                elif att_value == "false":
                    role.permissions.attach_files = False
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
            elif role_att == "read_message_history": # 15
                if att_value == "true":
                    role.permissions.read_message_history = True
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
                elif att_value == "false":
                    role.permissions.read_message_history = False
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
            elif role_att == "mention_everyone": # 16
                if att_value == "true":
                    role.permissions.mention_everyone = True
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
                elif att_value == "false":
                    role.permissions.mention_everyone = False
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
            elif role_att == "external_emojis": # 17
                if att_value == "true":
                    role.permissions.external_emojis = True
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
                elif att_value == "false":
                    role.permissions.external_emojis = False
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
            elif role_att == "connect": # 18
                if att_value == "true":
                    role.permissions.connect = True
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
                elif att_value == "false":
                    role.permissions.connect = False
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
            elif role_att == "speak": # 19
                if att_value == "true":
                    role.permissions.speak = True
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
                elif att_value == "false":
                    role.permissions.speak = False
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
            elif role_att == "mute_members": # 20
                if att_value == "true":
                    role.permissions.mute_members = True
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
                elif att_value == "false":
                    role.permissions.mute_members = False
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
            elif role_att == "deafen_members": # 21
                if att_value == "true":
                    role.permissions.deafen_members = True
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
                elif att_value == "false":
                    role.permissions.deafen_members = False
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
            elif role_att == "move_members": # 22
                if att_value == "true":
                    role.permissions.move_members = True
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
                elif att_value == "false":
                    role.permissions.move_members = False
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
            elif role_att == "use_voice_activation": # 23
                if att_value == "true":
                    role.permissions.use_voice_activation = True
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
                elif att_value == "false":
                    role.permissions.use_voice_activation = False
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
            elif role_att == "change_nickname": # 24
                if att_value == "true":
                    role.permissions.change_nickname = True
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
                elif att_value == "false":
                    role.permissions.change_nickname = False
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
            elif role_att == "manage_nicknames": # 25
                if att_value == "true":
                    role.permissions.manage_nicknames = True
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
                elif att_value == "false":
                    role.permissions.manage_nicknames = False
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
            elif role_att == "manage_roles": # 26
                if att_value == "true":
                    role.permissions.manage_roles = True
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
                elif att_value == "false":
                    role.permissions.manage_roles = False
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
            elif role_att == "manage_webhooks": # 27
                if att_value == "true":
                    role.permissions.manage_webhooks = True
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
                elif att_value == "false":
                    role.permissions.manage_webhooks = False
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
            elif role_att == "manage_emojis": # 28
                if att_value == "true":
                    role.permissions.manage_emojis = True
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
                elif att_value == "false":
                    role.permissions.manage_emojis = False
                    await self.client.edit_role(ctx.message.server, role, permissions = role.permissions)
            elif role_att == "none": # None
                await self.client.edit_role(ctx.message.server, role, permissions = role.permissions.none())
                await self.client.say("The role **%s** had the **%s** permissions set."%(role_name, role_att))
                return
            elif role_att == "all": # All
                await self.client.edit_role(ctx.message.server, role, permissions = role.permissions.all())
                await self.client.say("The role **%s** had the **%s** permissions set."%(role_name, role_att))
                return
            elif role_att == "all_channel": # All Channel
                await self.client.edit_role(ctx.message.server, role, permissions = role.permissions.all_channel())
                await self.client.say("The role **%s** had the **%s** permissions set."%(role_name, role_att))
                return
            elif role_att == "general": # General
                await self.client.edit_role(ctx.message.server, role, permissions = role.permissions.general())
                await self.client.say("The role **%s** had the **%s** permissions set."%(role_name, role_att))
                return
            elif role_att == "text": # Text
                await self.client.edit_role(ctx.message.server, role, permissions = role.permissions.text())
                await self.client.say("The role **%s** had the **%s** permissions set."%(role_name, role_att))
                return
            elif role_att == "voice": # Voice
                await self.client.edit_role(ctx.message.server, role, permissions = role.permissions.voice())
                await self.client.say("The role **%s** had the **%s** permissions set."%(role_name, role_att))
                return
            elif role_att == "hoist": # Hoist
                if att_value == "true":
                    await self.client.edit_role(ctx.message.server, role, hoist = True)
                elif att_value == "false":
                    await self.client.edit_role(ctx.message.server, role, hoist = False)
            elif role_att == "mentionable": # Mentionable
                if att_value == "true":
                    await self.client.edit_role(ctx.message.server, role, mentionable = True)
                elif att_value == "false":
                    await self.client.edit_role(ctx.message.server, role, mentionable = False)
            else:
                await self.client.say("The role attribute **%s** does not exist."%(role_att))
                return
            await self.client.say("The role **%s** had the permission **%s** set to **%s**."%(role_name, role_att, att_value))
        except Exception:
                await self.client.say("You do not have permission.")
        

def setup(client):
    client.add_cog(Roles(client))
