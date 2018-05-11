import os
import asyncio
import subprocess

os.system("rm main.py")
os.system("wget https://raw.githubusercontent.com/TSKsmiley/discord_weather_bot/e78e6bfa6b59fb099142d7c1dd791de8b1e0c64b/main.py")
os.system("python3 main.py")

#subprocess.check_output(['ls','-l']) #all that is technically needed...
print subprocess.check_output(['python3', 'main.py'])
