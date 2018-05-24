from discord.ext.commands import Bot
from discord import Game
from colorama import init
import discord
import random
import os
import sys
import requests
import json
import asyncio

VERSION = "0.1.4.7.0.1"
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

#Type bot prefix to use commands
BOT_PREFIX = ("?",",")
<<<<<<< HEAD
=======
BOT_TOKEN = Config['BOT_TOKEN']
>>>>>>> 91f3140356166b5c7314600a11de1d30b0eaf213
BOT_ID = Config['BOT_ID']
varMOTD = " "

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
            "It is certain"
            "It is decidedly so"
            "As I see it, yes"
            "You may rely on it"
            "Don't count on it"
            "Chances aren't good"
            "Better you not know"
            "Very doubtful"
            "It is not looking likely",
            "Too hard to tell",
            "It is quite possible",
            "Definitely",
            "I believe it is so",
            "I don't know but ramo is gay"
        ]
        await client.say(random.choice(possible_responses))

#credits
@client.command(
    name = "credits",
    description = "A list of people who helped with the bot",
    aliases = ["credits"]
)
async def credits():
    await client.say("The beautiful people who worked on the bot!\nThe Smiley Killer\nThe Lord Of Ducks")

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


#host
@client.command(
    name = "host"
)
async def host():
    await client.say(client.user.display_name + " is hosted on digital ocean: https://m.do.co/c/f69dc13cd3a6")


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
        await client.say("Updating! " + ctx.message.author.mention)
        await client.change_presence(game=Game(name="Updating.."), status="invisible")
        print("UPDATING...")
        await asyncio.sleep(2)
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
        varMOTD = newMOTD
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
    discord.Member
    #sending messages out
    ownerid = "<@174427069747429376>"
    await client.send_message(discord.Member.User("<@174427069747429376>"), str("Ready! ``Version: " + VERSION + "``"))
    #await client.send_message(message.Config['DEV_ID'], str("Ready! ``Version: " + VERSION + "``"))




#========= Other ========

#running the bot
client.run(BOT_TOKEN)

#auto updating and restarting (linux)
if(os.name != "nt"):
    os.system("rm updt.py")
    asyncio.sleep(1)
    os.system("wget https://raw.githubusercontent.com/TSKsmiley/discord_bot/master/updt.py")
    asyncio.sleep(1)
    os.system("python3 updt.py")

