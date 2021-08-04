# Libraries
import random
import os
import sys
from getkey import getkey
from time import sleep

# Clear interface
def clear():
	os.system('clear')

# SlowPrint function
def SlowPrint(text, slptime):
	for i in text:
		sys.stdout.write(i)
		sys.stdout.flush()
		sleep(slptime)

# Colors
White="\033[0;37m" 
Cyan="\033[1;36m"
Green="\033[0;32m"
Orange ="\033[0;33m"
Pink = "\033[1;31m"

# Banner
def banner():
	print("(¯`·._.··¸.-~*´¨¯¨`*·~-.,-( XTREME SPORTS )-,.-~*´¨¯¨`*·~-.¸··._.·´¯)")
	sleep(7.5)



# Mini Display Screen
login0 = '''
╔════════════════════════════╗
║                            ║
║ Login: Player              ║
║ Password:                  ║
║                            ║
╚════════════════════════════╝
'''
login1 = '''
╔════════════════════════════╗
║                            ║
║ Login: Player              ║
║ Password: *                ║
║                            ║
╚════════════════════════════╝
'''
login2 = '''
╔════════════════════════════╗
║                            ║
║ Login: Player              ║
║ Password: **               ║
║                            ║
╚════════════════════════════╝
'''
login3 = '''
╔════════════════════════════╗
║                            ║
║ Login: Player              ║
║ Password: ***              ║
║                            ║
╚════════════════════════════╝
'''
login4 = '''
╔════════════════════════════╗
║                            ║
║ Login: Player              ║
║ Password: ****             ║
║                            ║
╚════════════════════════════╝
'''
login5 = '''
╔════════════════════════════╗
║                            ║
║ Login: Player              ║
║ Password: *****            ║
║                            ║
╚════════════════════════════╝
'''
login6 = '''
╔════════════════════════════╗
║                            ║
║ Login: Player              ║
║ Password: *****            ║
║                            ║
╚════════════════════════════╝
'''
login7 = '''
╔════════════════════════════╗
║                            ║
║           LOGIN            ║ 
║         SUCCESSFUL         ║
║                            ║
╚════════════════════════════╝
'''
login8 = '''
╔════════════════════════════╗
║                            ║
║           WELCOME          ║ 
║                            ║
║                            ║
╚════════════════════════════╝
'''

# Login Process
def login():
	clear()
	print(login0)
	sleep(1)
	clear()
	print(login1)
	sleep(0.5)
	clear()
	print(login2)
	sleep(0.5)
	clear()
	print(login3)
	sleep(0.5)
	clear()
	print(login4)
	sleep(0.5)
	clear()
	print(login5)
	sleep(0.5)
	clear()
	print(login6)
	sleep(0.5)
	clear()
	print(login7)
	sleep(1)
	clear()
	print(login8)
	sleep(1.7)
	clear()

# Initialization Process
def intro():
	for i in range(31):
		clear()
		print("Initializing...")

banner()
login()
intro()
print("\n")
sleep(3)
clear()
SlowPrint(White + 'Enter your name: ' + Green, 0.08)
name = input()

print("\n\n")
clear()

print(Pink + "Choose one of two available Xtreme Sports:\n")

# Unpack Options
Sports = ["Surf GX", "Marathon BL"]
y, s = Sports
print(Cyan + y)
print(Cyan + s)
print(White + "\n\nChose by name" + Green)
option = input()

clear()

if option == "Surf GX":
	SlowPrint(Orange + "You chose 'Surf GX'.", 0.08)
	sleep(1)
	SlowPrint(Pink + "In this game, you must guide your surfer through high tide.", 0.08)
	sleep(0.25)
	clear()
	sleep(0.5)
	print("					🏄")


