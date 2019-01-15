import discord
import json
from discord.ext import commands
import asyncio
import os
import itertools
import random
authorized_users = [
    "271987926026420224"
    "303917352964194305"
]

client = commands.Bot(command_prefix = 'b!')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='b!help | 211 Servers.'))
    await asyncio.sleep(5)
    await client.change_presence(game=discord.Game(name='So much Coding.'))
    await asyncio.sleep(5)
    print('Ready, Freddy.')
    
@client.event
async def on_message(message):
    if ('cock') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('penis') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('fuck') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('vagina') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('motherfucker') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('fucker') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('tits') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('fucking') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('dick') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('anal') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('porn') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('pussy') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if message.content == 'b!ping':
        await client.send_message(message.channel,'Pong!')
    if message.content == 'b!version':
        await client.send_message(message.channel,'Current Version: **Jarvis 2.3**')
    if message.content == 'b!credits':
        await client.send_message(message.channel,'**Credits to WolfHussain for creating me with such IQ and thinking ability. Thank him please :)**')
    if message.content == 'b!servercount':
        await client.send_message(message.channel,'*Currently working for approximatly 212 Servers*')
    await client.process_commands(message)

@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('*Messages Deleted, Sir.*')

@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, user: discord.Member, *, arg = None):
    if arg is None:
        await client.say("Please provide a reason for {}'s warning.".format(user.name))
        return False
    reason = arg
    author = ctx.message.author
    server = ctx.message.server
    embed = discord.Embed(title="Warn", description=" ", color=0x00ff00)
    embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
    embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
    embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
    await client.say(embed=embed)
    await client.send_message(user, "You have been warned for: {}".format(reason))
    await client.send_message(user, "from: {} server".format(server))

@client.command(pass_context=True)
async def info():
    embed = discord.Embed(
        title = 'Name:',
        description = 'Jarvis#3765',
        colour = discord.Colour.blue()
    )

    embed.set_image(url='https://cdn.discordapp.com/attachments/434288295548026886/529380566244655114/images.jpg')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/434288295548026886/529380566244655114/images.jpg')
    embed.set_author(name='Information Section:',
    icon_url='https://cdn.discordapp.com/attachments/434288295548026886/529380566244655114/images.jpg')
    embed.add_field(name='Creator:', value='Yo#0953.', inline=False)
    embed.add_field(name='Creation Date:', value='12th Dec 2018.', inline=False)
    embed.add_field(name='Coded from:', value='3.6.5 Python Shell.', inline=False)

    await client.say(embed=embed)

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.command(pass_context=True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()

@client.command(pass_context=True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id].stop()

@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()

@client.command(pass_context=True)
async def playerinfo(ctx, user: discord.Member):
    embed = discord.Embed(title='{} Info:'.format(user.name), description='Here is  what i could find, Sir.', color=0x00ff00)
    embed.add_field(name='Name:', value='user.name', inline=False)
    embed.add_field(name='ID:', value='user.id', inline=False)
    embed.add_field(name='Status:', value='user.status', inline=False)
    embed.add_field(name='Highest Role:', value='user.top_role', inline=False)
    embed.add_field(name='Joined At:', value='user.joined_at', inline=False)
    embed.add_thumbnail(url='user.avatar_url')

@client.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(
        title = 'Server Information:',
        description = 'Information is on its way!',
        colour = discord.Colour.blue()
    )

    embed.set_image(url='https://cdn.discordapp.com/attachments/434288295548026886/529380566244655114/images.jpg')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/434288295548026886/529380566244655114/images.jpg')
    embed.set_author(name='Server Information:',
    icon_url='https://cdn.discordapp.com/attachments/434288295548026886/529380566244655114/images.jpg')
    embed.add_field(name='Server Name:', value='Custom Discord Bot Testing Server.', inline=False)
    embed.add_field(name='Creation Date:', value='4th Dec 2018.', inline=False)
    embed.add_field(name='Made By:', value='Discord | Discord, Please Sponser Me.', inline=False)
    embed.add_field(name='ID:', value='ctx.message.server.id', inline=False)
    embed.add_field(name='Roles:', value='len(ctx.message.server.roles)', inline=False)
    embed.add_field(name='Members:', value='len(ctx.message.server.members)', inline=False)

    await client.say(embed=embed)
    
@client.command(pass_context=True)
async def mute(ctx, member: discord.Member):
    if ctx.message.author.id in authorized_users:
        role = discord.utils.get(member.server.roles, name="Muted")
        await client.add_roles(user, role)
        embed = discord.Embed(title="Mute", description="Successful", color=0x149900)
        embed.add_field(name="User", value=member.id, inline=False)
        await client.say(embed=embed)
    else:
        embed = discord.Embed(title="Error", description="You do not have permission to use that command, {}.".format(ctx.message.author.name), color=0x990000)
        await client.say(embed=embed)
        
@client.command(pass_context=True)
async def unmute(ctx, member: discord.Member):
    if ctx.message.author.id in authorized_users:
        role = discord.utils.get(member.server.roles, name="Muted")
        await client.remove_roles(user, role)
        embed = discord.Embed(title="Unmute", description="Successful", color=0x149900)
        embed.add_field(name="User", value=member.id, inline=False)
        await client.say(embed=embed)
    else:
        embed = discord.Embed(title="Error", description="You do not have permission to use that command, {}.".format(ctx.message.author.name), color=0x990000)
        await client.say(embed=embed)
        
@client.command(pass_context=True)
async def ban(ctx, member: discord.Member, days: int = 1):
    if ctx.message.author.id in authorized_users:
        await client.ban(member, days)
        embed = discord.Embed(title="Ban", description="Successful", color=0x149900)
        embed.add_field(name="User", value=member.id, inline=False)
        await client.say(embed=embed)
    else:
        embed = discord.Embed(title="Error", description="You do not have permission to use that command, {}.".format(ctx.message.author.name), color=0x990000)
        await client.say(embed=embed)
        
@client.command(pass_context=True)
async def unban(ctx, *, member):
    if ctx.message.author.id in authorized_users:
        server = ctx.message.server
        bans = await client.get_bans(server)
        try:
            uid = int(member)
            uid = str(uid)
            matches = list(filter(lambda u: u.id == uid, bans))
            if not matches:
                return await client.say('no users ids matched with %s' % uid)
            _member = matches[0]
        except ValueError:
            matches = list(filter(lambda u: str(u) == member, bans))
            if not matches:
                return await client.say('no users matched with %s' % member)
            _member = matches[0]
        await client.unban(ctx.message.server, _member)
        embed = discord.Embed(title="Unban", description="Successful", color=0x149900)
        embed.add_field(name="User", value=member.id, inline=False)
        await client.say(embed=embed)
    else:
        embed = discord.Embed(title="Error", description="You do not have permission to use that command, {}.".format(ctx.message.author.name), color=0x990000)
        await client.say(embed=embed)
        
@client.command(pass_context=True)
async def kick(ctx, member: discord.Member):
    if ctx.message.author.id in authorized_users:
        await client.kick(member)
        embed = discord.Embed(title="Kick", description="Successful", color=0x149900)
        embed.add_field(name="User", value=member.id, inline=False)
        await client.say(embed=embed)
    else:
        embed = discord.Embed(title="Error", description="You do not have permission to use that command, {}.".format(ctx.message.author.name), color=0x990000)
        await client.say(embed=embed)
        
@client.command(pass_context=True)
async def ping(ctx):
    t = await client.say('Pong!')
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
    await client.delete_message(t)
    embed = discord.Embed(title="Ping", description="Pong", color=0x149900)
    embed.add_field(name="Latency", value=str(int(ms)) + " ms", inline=False)
    await client.say(embed=embed)
    print(f'Ping {int(ping)}ms')
    
@client.command(pass_context=True)
async def punch(ctx, user: discord.Member):
    embed = discord.Embed(title="Now Punching", description=user.mention, color=0x149900)
    await client.say(embed=embed)
    embed_2 = discord.Embed(title="You've been punched!", description="By " + ctx.message.author.name, color=0x149900)
    await client.send_message(user, embed=embed_2)
    
@client.command(pass_context=True)
async def members(ctx):
    embed = discord.Embed(title="Member Count", description=str(len(ctx.message.server.members)), color=0x149900)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def help(ctx):
    await client.say('Help is on its way! Check your DM.')
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()

    )

    embed.set_author(name='Help | Commands')
    embed.add_field(name='b!info', value='Gives you information about me.', inline=False)
    embed.add_field(name='b!playerinfo', value='Gives you information about the player.', inline=False)
    embed.add_field(name='b!serverinfo', value='Gives you information about the server.', inline=False)
    embed.add_field(name='b!ping', value='Gives you information about my Latency.', inline=False)
    embed.add_field(name='b!ban', value='Bans a player.', inline=False)
    embed.add_field(name='b!unban', value='Unbans a player.', inline=False)
    embed.add_field(name='b!kick', value='Kicks a player.', inline=False)
    embed.add_field(name='b!mute', value='Mutes a player.', inline=False)
    embed.add_field(name='b!unmute', value='Unmutes a player.', inline=False)
    embed.add_field(name='b!warn', value='Warns a player.', inline=False)
    embed.add_field(name='b!purge', value='Clears a message.', inline=False)
    embed.add_field(name='b!join', value='Joins the channel.', inline=False)
    embed.add_field(name='b!leave', value='Leaves the channel.', inline=False)
    embed.add_field(name='b!play {url}', value='Plays the music you want the bot to play in the url.', inline=False)
    embed.add_field(name='b!pause', value='Pauses the music.', inline=False)
    embed.add_field(name='b!stop', value='Stops the music.', inline=False)
    embed.add_field(name='b!resume', value='Resumes the music.', inline=False)
    embed.add_field(name='b!punch {member}', value='Punchs the member.', inline=False)
    embed.add_field(name='b!membercount', value='Gives you the member count of the server.', inline=False)
    embed.add_field(name='b!credits', value='Gives you credits to who made me.', inline=False)
    embed.add_field(name='b!servercount', value='Gives you the amount of servers i am working for.', inline=False)
    embed.add_field(name='b!version', value='Gives you the version of me.', inline=False)

    await client.send_message(author, embed=embed)
    
client.run('NTI5MzYzMTI1NTMxNTc0Mjcy.Dwvv1g.RtRLv_pMI3MuCc1RyuKcn7qOYXM')
