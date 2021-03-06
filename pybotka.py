#!/bin/env python3

import discord
import os
from dotenv import load_dotenv
from os import getenv
from sys import stderr

def eprint(*args, **kwargs):
    print(*args, file=stderr, **kwargs)

def startsWith(string, char):
    if string[0] == char:
        return True
    return False

def startsWith2Char(string, char):
    try:
        if string[0] == char[0] and string[1] == char[1]:
            return True
    except IndexError:
        pass
    return False

def ltoString(listt):
    string = " "
    for i in listt:
        string += " " + i
    return string

def removeFirstChar(string):
    return string[1:]

##### BEGIN CMDS #####

class Command():
    cmd: str
    message: str
    def __init__(self, cmd, message):
        self.cmd     = cmd
        self.message = message

default = Command(cmd="", message="")
added_commands = [default]

cmd_list = [
    "!ping",
    "!help",
    "!whatIsInNsfw",
    "!cpp",
    "!rust",
    "!python",
    "!anime",
    "!riir",
    "!whoami",
    "!killme",
    "!about",
    "!chelp",
    "!ban",
    "!addcmd"
]

######################

##### BEGIN BOT #####

load_dotenv()
TOKEN = getenv("DISCORD_TOKEN")
GUILD = getenv("DISCORD_GUILD")

client = discord.Client()

adm = "<@948968646594658334>"

about = """
:red_circle: **CHATS**:

#sobre - aqui

#link-para-convite - link para compartilhar o servidor

:speaker: Mr Strimmer - transmissões de quem possui o cargo @MrStrimmer

#annoycements - avisos de @ele

#regras - 3RROR

#geral - qualquer coisa

#memes - chat para compartilhar memes

#jogos - chat para compartilhar screenshots, gameplays, e convites sobre jogos

#anime - para conversar sobre anime

#arte - chat para compartilhar desenhos, música (de autoria própria), e vídeos artísticos

#musica - chat para compartilhar músicas que você gosta

#compartilhar - chat para compartilhar links com outras pessoas

#programacao - chat para compartilhar e obter ajuda com programação (sem malwares ok)

:speaker: Geral - canal para conversar sobre o que quiser através de voz

:speaker: Baderna - canal sem regras, faça o que quiser

#1, #2, #3, #4 - chat para conversar sobre trabalhos de escola

:speaker: voz - canal de voz para trabalhos de escola

#english - chat to talk in english

#divulgação - divulgar vídeos ou lives de @youtuber/streamer

#sus - A̴̾͐M̶̜̿Ö̶́͛G̸͋͐U̶̓͐Ś̴͛

#nsfw - NO
"""

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(f"{client.user} is online!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # commands
    if startsWith(message.content, "!"):
        args = message.content.split()
        command = removeFirstChar(args[0])

        if command == "ping":
            await message.channel.send("Pong!")
        elif command == "help":
            helpp = ""
            for h in cmd_list:
                helpp += " " + h
            await message.channel.send(helpp)
        elif command == "whatIsInNsfw":
            await message.channel.send("Po$$, nu$$$$, and h$$$ai")
        elif command == "cpp":
            await message.channel.send("**Rust**")
        elif command == "rust":
            await message.channel.send("https://rustrecoveryfoundation.neocities.org/")
        elif command == "python":
            await message.channel.send("loading...")
        elif command == "anime":
            await message.channel.send("H$$$ai is only for +18")
        elif command == "whoami":
            await message.channel.send(f"Of course you are {message.author}")
        elif command == "killme":
            await message.channel.send(f"{message.author} was killed by {client.user}")
        elif command == "install":
            try:
                await message.channel.send(f"{args[1]} was installed successfully")
            except IndexError:
                await message.channel.send(f"ERROR: Argument not provided for `!install`")
        elif command == "about":
            await message.channel.send(about)
        elif command == "riir":
            try:
                await message.channel.send(f"Have you considered rewriting {args[1]} in rust?")
            except IndexError:
                await message.channel.send(f"ERROR: Argument not provided for `!riir`")
        elif command == "chelp":
            try:
                await message.channel.send(f"<@948968646594658334>: {ltoString(args[1:])}")
            except IndexError:
                await message.channel.send(f"ERROR: Argument not provided for `!chelp`")
        elif command == "ban":
            try:
                if message.author.id == 948968646594658334:
                    user_banned_id = ""
                    if startsWith2Char(args[1], "<@"):
                        for c in args[1]:
                            if c == ">":
                                break
                            elif c not in "<@":
                                user_banned_id += c
                    user_banned = await client.fetch_user(int(user_banned_id))
                    await message.guild.ban(user_banned)
                    await message.channel.send(f"{user_banned.name} was banned")
                else:
                    await message.channel.send(f"Only {adm} XD")
            except Exception as ex:
                await message.channel.send(f"ERROR: {ex}")
        elif command == "addcmd":
            try:
                if message.author.id == 948968646594658334:
                    addcmd = Command(cmd=args[1],message=ltoString(args[2:]))
                    added_commands.append(addcmd)
                    cmd_list.append("!" + args[1])
                    await message.channel.send(f"Added command {args[1]}")
                else:
                    await message.channel.send(f"Only {adm} XD")
            except IndexError:
                await message.channel.send(f"ERROR: Argument not provided for `addcmd`")
        else:
            error = False
            for cmd in added_commands:
                if command == cmd.cmd:
                    await message.channel.send(cmd.message)
                    error = False
                    break
                else:
                    error = True
            if error:
                await message.channel.send(f"ERROR: Unknown command: `{command}`")


client.run(TOKEN)

#####################
