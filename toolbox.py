#!/usr/bin/env python3
from nmap.nmap import nmap

print("Welcome To ToolBox! \nPlease choose a option. \n1: nmap \n2: hydra\n3: burpsuite")

user_input = input("use: ")

while True:
  if user_input == "1":
     ip_input = input("ip:")	
     nmap(ip_input)
     break
  elif user_input == "2":
     print("hydra")
     break
  elif user_input == "3":
     print("burpsuite")
     break
  else: 
     print("please enter a valid option")
     user_input = input("use: ")	
