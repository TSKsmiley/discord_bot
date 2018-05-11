import os

async def update_and_run():
    await os.system("rm main.py")
    await os.system(
        "wget https://raw.githubusercontent.com/TSKsmiley/discord_weather_bot/master/main.py")
    await os.system("python3 main.py")
    exit()

update_and_run()