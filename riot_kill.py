import subprocess
from time import sleep
from tkinter import N

import psutil

for proc in psutil.process_iter():
    if proc.name() == "LeagueClient.exe":
        proc.kill()
        print("Killed")
path = "D:\\Riot Games\\League of Legends\\LeagueClient.exe"
subprocess.run([path])
