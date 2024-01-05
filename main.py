#!/usr/bin/env python3
from nmap.nmap import nmap
from update_packages.update_packages import update_packages
print(r'''
      / \__
     (    @\___
     /         O
    /   (_____/
   /_____/   U
''')


print("Welcome To ToolBox! \nPlease choose a option.\n1: Install programs \n2: nmap \n3: hydra\n4: burpsuite")

user_input = input("use: ")

while True:
  if user_input == "1":
     update_packages()
    
  elif user_input == "2":
     ip_input = input("ip:")	
     nmap(ip_input)
     break
  elif user_input == "3":
     print("hydra")
     break
  elif user_input == "4":
     print("burpsuite")
     break
  else: 
     print("please enter a valid option")
     user_input = input("use: ")	
