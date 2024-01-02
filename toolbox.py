#!/usr/bin/env python3
from nmap.nmap import nmap

print("Welcome to ToolBox! \nPlease choose a option. \n1: nmap \n2: hydra\n3: burpsuite")

userInput = input("use: ")

if userInput == "1":
    nmap()
elif userInput == "2":
    print("hydra")
elif userInput == "3":
    print("burpsuite")
else: 
    print("please enter a valid option")
