import os

os.system("rm main.py")
time.sleep(0.2)
os.system("wget https://raw.githubusercontent.com/TSKsmiley/discord_weather_bot/master/main.py")
time.sleep(8)
os.system("python3 main.py")
exit()
