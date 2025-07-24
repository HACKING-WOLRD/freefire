# -*- coding: utf-8 -*-
# FREE FIRE HACKING TOOL (FAKE/PRANK)
# HACKING WORLD™ - SHOW OFF TOOL

import os, time

G = '\033[1;32m'
R = '\033[1;31m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'
P = '\033[95m'

def banner():
    os.system("clear")
    print(f"""{G}
███████╗███████╗     ██╗███████╗██╗██████╗ 
██╔════╝██╔════╝     ██║██╔════╝██║██╔══██╗
█████╗  █████╗       ██║█████╗  ██║██████╔╝
██╔══╝  ██╔══╝  ██   ██║██╔══╝  ██║██╔═══╝ 
███████╗███████╗ ╚█████╔╝███████╗██║       
╚══════╝╚══════╝  ╚════╝ ╚══════╝╚═╝       
   {P}HACKING WORLD - FREE FIRE ID HACK TOOL
{W}--------------------------------------------------""")

def main():
    banner()
    uid = input(f"{C}Enter Target Free Fire UID: {W}")
    print(f"\n{Y}[+] Connecting to Free Fire secure server...")
    time.sleep(2)
    print(f"{G}[✓] UID found: {uid}")
    time.sleep(1.5)
    print(f"{Y}[!] Checking account status...")
    time.sleep(2)
    print(f"{R}[!] Account is active & secured!")
    time.sleep(1)
    print(f"{P}[✓] Hack path found via UID")
    time.sleep(1.5)

    print(f"\n{R}[⚠] Credit Required: 500৳ to unlock hacking module.")
    ask = input(f"{Y}Do you want to continue? (yes/no): {W}")
    if ask.lower() == "yes":
        print(f"\n{C}Redirecting to WhatsApp Admin...\n")
        time.sleep(2)
        os.system("xdg-open 'https://wa.me/8801XXXXXXXXX'")  # WhatsApp your number here
    else:
        print(f"\n{R}Operation Cancelled.")
        exit()

if __name__ == "__main__":
    main()