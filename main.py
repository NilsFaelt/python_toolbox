#!/usr/bin/env python3
from nmap.nmap import nmap
from dirbuster.dirbuster import dirbuster
from update_packages.update_packages import update_packages
dogs = r'''
               Nils ToolBox

      / \__       / \__        / \__
     (    @\___  (    @\___   (    @\___
     /         O  /         O  /         O
    /   (_____/  /   (_____/  /   (_____/
   /_____/   U  /_____/   U  /_____/


         Use Only for legal purposes
'''

print(dogs)



print("Welcome! \nPlease choose a option.\n1: Install packages \n2: nmap \n3: hydra\n4: burpsuite\n5: dirbuster")

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
  elif user_input == "5":
     ip_input = input("ip:")	
     dirbuster(ip_input)
     break
  else: 
     print("please enter a valid option")
     user_input = input("use: ")	
