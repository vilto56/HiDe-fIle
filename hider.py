#!/usr/bin/python3
#coded by Sayuk Beast

#requirements
import os
from time import sleep
from sys import exit

cya = "\033[1;32;40mBye Hope See you again :)."
nopt = "\033[1;31;40m[!]Sorry No Such of option"
green = "\033[1;32;40m"
red = "\033[1;31;40m"
black = "\033[1;30;40m"
yellow = "\033[1;33;40m"
blue = "\033[1;34;40m"
purple = "\033[1;35;40m"
cyan = "\033[1;36;40m"
white = "\033[1;37;40m"
normal = "\033[0m"

def logo():
  os.system("clear")
  print("\033[1;32;40m ____                    _    ____                 _")
  sleep(0.1)
  print("/ ___|  __ _ _   _ _   _| | _| __ )  ___  __ _ ___| |_")
  sleep(0.1)
  print("\___ \ / _` | | | | | | | |/ /  _ \ / _ \/ _` / __| __|")
  sleep(0.1)
  print(" ___) | (_| | |_| | |_| |   <| |_) |  __/ (_| \__ \ |_")
  sleep(0.1)
  print("|____/ \__,_|\__, |\__,_|_|\_\____/ \___|\__,_|___/\__|")
  sleep(0.1)
  print("             |___/")
  sleep(0.1)
  print("Tool created by Sayuk Beast")
  print()
  print("\033[1;31;40m Do not copy this code without my permission")
  print("Please appreciate my hard work")
  print()
def start():
  start = input(yellow+"[?]Do You Want To Start? Y/n ")
  if start == "y" or start == "":
     main()
  if not start == "y" or start == "":
     exit()
def main():
  print(green+"Choose Your Option")
  print(cyan+"1 = embed")
  print("2 = extract")
  choose = input(yellow+"option >> ")
  if choose == "1":
     first()
  if choose == "2":
     second()
  if not choose == "1" or choose == "2":
     print(nopt)
     sleep(1)
     os.system("clear")
     main()
def first():
  ef = input(yellow+"Choose Your File To Be Hide [path] ")
  cf = input("Choose Your Images To Be Embed With Your File [path] ")
  os.system("steghide embed -cf "+cf+" -ef "+ef)
def second():
  sf = input("What Is Your File Name?")
  os.system("steghide extract -sf "+sf)
def end():
  print("Closing...")
  sleep(1)
  print(cya)
  sleep(1)
  os.system("clear")
#def
try:
  logo()
  start()
except KeyboardInterrupt:
  end()
