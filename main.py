#!/usr/bin/env python3
"""Toolbox"""
import asyncio
from nmap.nmap import nmap
from gobuster.gobuster import gobuster
from update_packages.update_packages import update_packages
from packages_and_info.packages_and_info import packages_and_info
from metasploit.metasploit import metasploit
from wpscan.wpscan import wpscan
from util_functions.scan_curl_for_users import scan_curl_for_users
from get_pokemon.get_pokemon import get_pokemon
from password_cracker.password_cracker import password_cracker
DOGS = r'''
               Gemina ToolBox

      / \__       / \__        / \__
     (    @\___  (    @\___   (    @\___
     /         O  /         O  /         O
    /   (_____/  /   (_____/  /   (_____/
   /_____/   U  /_____/   U  /_____/


         Use Only for legal purposes
'''

print(DOGS)



def display_menu():
    """Function printing menu options."""
    print("Welcome!\nPlease choose an option")
    print("Choose option 1 first time you use this toolbox to install all tool/packages\n")
    print("0: Info\n1: install packages/tools:")
    print("2: nmap\n3: metasploit\n4: wpscan\n5: dirbuster\n6: curl scan for users\n7: Pokemon api")
    print("8: password cracker")
def main():
    """Function accepting user_input for menu"""
    while True:
        display_menu()
        user_input = input("Select an option: ")

        if user_input == "0":
            packages_and_info()
        elif user_input == "1":
            update_packages()
        elif user_input == "2":
            ip_input = input("Enter IP: ")
            nmap(ip_input)
        elif user_input == "3":
            metasploit()
        elif user_input == "4":
            ip_input = input("Enter IP: ")
            wpscan(ip_input)
        elif user_input == "5":
            ip_input = input("Enter IP: ")
            gobuster(ip_input)
        elif user_input == "6":
            adress = input("Enter Adress:")
            scan_curl_for_users(adress)
        elif user_input == "7":
            user_input = input("Enter pokemon name please:")
            async def get_pokemon_wrapper():
                await get_pokemon(user_input)
            if __name__ == "__main__":
                asyncio.run(get_pokemon_wrapper())
        elif user_input == "8":
            user_input = input("Enter sha-256 hash please")
            password_cracker(user_input)
        else:
            print("Please enter a valid option.")
        choice = input("Do you want to continue? (y/n): ").lower()
        if choice != 'y':
            break

if __name__ == "__main__":
    main()
