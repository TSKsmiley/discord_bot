from discord.ext.commands import Bot
from discord import Game
from colorama import init
import random
import os
import sys
import requests
import json
import asyncio

VERSION = "0.1.3"
#starting colorama
init()


#os specific commands
os.system('cls' if os.name == 'nt' else 'clear')
os.system('title Discord TSK bot' if os.name ==
          'nt' else 'not windows')
#defining terminal colors

class termcol:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#========= different variables for the bot ==========
with open('Config.json') as f:
    Config = json.load(f)


BOT_PREFIX = ("?",",")
BOT_TOKEN = Config['BOT_TOKEN']
BOT_ID = Config['BOT_ID']
MOTD = " "

print(Config['OWNER_ID'])

async def AuthorisedUser(userID):
    if str(userID) == str(Config['OWNER_ID']) or str(userID) == "234733470650204160":
        return True
    else:
        await client.say("Invalid permissions this command is only for the bot Devs")
        return False



#defing bot "name" and prefix and printing
client = Bot(BOT_PREFIX)
print("\n\n===================" + termcol.OKGREEN + "  TSK " +
      termcol.OKBLUE + " DISCORD BOT " + termcol.ENDC + "===================")
print("Attempting login with token: " + termcol.WARNING + BOT_TOKEN + termcol.ENDC + "\n=========================================================")
print(VERSION)

#===== Bot Commands =====

#8ball
@client.command(
    name = "8ball",
    description = "Answers a yes/no question",
    brief = "Answers from...",
    aliases = ["8-ball", "eightball", "eight_ball"]
)
async def eight_ball():
        possible_responses = [
            "That is a no",
            "It is not looking likely",
            "Too hard to tell",
            "It is quite possible",
            "definitely",
            "I don't know but ramo is gay"
        ]
        await client.say(random.choice(possible_responses))


#github command [random text to fool the github raw]
@client.command(
    name = "github",
    aliases = ["todo", "to-do", "git"])
async def github():
    await client.say("information about the development of this bot is at the github page: https://github.com/TSKsmiley/discord_bot/projects/1")


#what is the meaning tho
@client.command
async def whatisthemeaningoflife():
    await client.say("42")


#MOTD
#@client.command(
#    name = "motd",
#    aliases = ["motd", "message_of_the_day"]
#)
#async def motd():
#    await client.say("MOTD: ``" + MOTD + "``")


#NOT WORKING rollme command
#@client.command()
#async def rollme():
#    await client.say("!play https://www.youtube.com/watch?v=dQw4w9WgXcQ")

#math command
@client.command(
    name = "math",
    description = "a calculator command",
    pass_context = True,
    aliases = "m"
)
async def math(ctx, firstNUM, operator, secondNUM):
    intFirstnum = int(firstNUM)
    intSecondnum = int(secondNUM)
    if operator == "*":
        answer = int(intFirstnum * intSecondnum)
    elif operator == "/":
        answer = int(intFirstnum / intSecondnum)
    elif operator == "+":
        answer = int(intFirstnum + intSecondnum)
    elif operator == "-":
        answer = int(intFirstnum - intSecondnum)
    elif operator == "^":
        answer = int(intFirstnum ^ intSecondnum)
    
    await client.say(answer)




#===== Special dev commands =====

#update
@client.command(name = "update",
                pass_context=True,
                aliases = ["restart", "reboot", "updt"]
                )
async def update(ctx):
    print(ctx.message.author.id + "\n" + str(Config['OWNER_ID']))
    if AuthorisedUser(ctx.message.author.id):
        await client.change_presence(game=Game(name="Updating.."), status="invisible")
        await client.say("Updating! " + ctx.message.author.mention)
        print("UPDATING...")
        await client.logout()
 

#set-motd
@client.command(
    name = "setmotd",
    aliases = ["set-motd", "smotd", "s-motd"],
    biref = "dev only command",
    pass_context = True
)
async def set_motd(ctx, newMOTD):
    if AuthorisedUser(ctx.message.author.id):
        MOTD = newMOTD
        await client.say("MOTD is now set to: " + MOTD)


#Set game
@client.command(
    name = "setgame",
    aliases = ["game","changegame"],
    description = "A owner only command",
    brief = "owner only command",
    pass_context = True
    )
async def setgame(ctx, gamename):
    if AuthorisedUser(ctx.message.author.id):
        await client.change_presence(game=Game(name=gamename))
        print(termcol.WARNING + "Set game to:" + gamename + termcol.ENDC)



#======== events ========
@client.event
async def on_ready():
    print(termcol.OKGREEN + "Logged it as: " + client.user.display_name + termcol.ENDC)
    await client.change_presence(game=Game(name="Prefixes = , and ?"))


@client.event
async def on_error(error):
    print(termcol.WARNING + "ERROR:" + error + termcol.ENDC)

#running the bot
client.run(BOT_TOKEN)

#auto updating and restarting (linux)
if(os.name != "nt"):
    os.system("rm updt.py")
    asyncio.sleep(1)
    os.system("wget https://raw.githubusercontent.com/TSKsmiley/discord_bot/master/updt.py")
    asyncio.sleep(1)
    os.system("python3 updt.py")

