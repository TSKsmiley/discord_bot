import os
import asyncio

#updater program
async def test():
    os.system("rm main.py")
    await asyncio.sleep(1)
    os.system("wget https://raw.githubusercontent.com/TSKsmiley/discord_weather_bot/master/main.py")
    await asyncio.sleep(9)
    os.system("python3 main.py")
    exit()
#done
async test()