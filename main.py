from discord.ext.commands import Bot
from discord import Game
from colorama import init
import random
import os
import sys
import requests
#starting colorama
init()


#os specific commands
os.system('cls' if os.name == 'nt' else 'clear')
os.system('title Discord TSK bot' if os.name ==
          'nt' else 'echo "^[]0;Discord TSK bot^G"')
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
BOT_PREFIX = ("?",",")
BOT_TOKEN = ("NDIyNzQ3NDg1OTg4MTkyMjY2.DdTF3A.3tX16Y345-9RSBSy2suGkQslrKc")
BOT_ID = ("422747485988192266")
AUTHOR_ID = ("174427069747429376")

#defing bot "name" and prefix and printing
client = Bot(BOT_PREFIX)
print("\n\n===================" + termcol.OKGREEN + "  TSK " +
      termcol.OKBLUE + " DISCORD BOT " + termcol.ENDC + "===================")
print("Attempting login with token: " + termcol.WARNING + BOT_TOKEN + termcol.ENDC + "\n=========================================================")

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
            "defenetly"
        ]
        await client.say(random.choice(possible_responses))

#weather command



#Special dev commands
@client.command(name = "stop",
                pass_context=True,
                )
async def stop(ctx):
    if ctx.message.author.id == AUTHOR_ID:
        await client.change_presence(game=None, status="invisible")
        await client.say("STOPPING! " + ctx.message.author.mention)
        exit()
    else:
        await client.say("Invalid permissions \nthis command is only for the bot owner")

@client.command(
    name = "setgame",
    aliases = ["game","changegame"],
    description = "A owner only command",
    brief = "owner only command",
    pass_context = True
    )
async def setgame(ctx, gamename):
    if ctx.message.author.id == AUTHOR_ID:
        await client.change_presence(game=Game(name=srt(gamename)))
        print(gamename)
    else:
        await client.say("Invalid permissions \nthis command is only for the bot owner")


#events
@client.event
async def on_ready():
    print(termcol.OKGREEN + "Logged it as: " + client.user.display_name + termcol.HEADER)
    await client.change_presence(game=Game(name="Prefixes = , and ?"))


@client.event
async def on_error(error):
    print(termcol.WARNING + "ERROR:" + error)

#running the bot
client.run(BOT_TOKEN)
