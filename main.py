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



def display_menu():
    print("Welcome!\nPlease choose an option.")
    print("1: Install packages\n2: nmap\n3: hydra\n4: burpsuite\n5: dirbuster")

def main():
    while True:
        display_menu()
        user_input = input("Select an option: ")

        if user_input == "1":
            update_packages()
        elif user_input == "2":
            ip_input = input("Enter IP: ")
            nmap(ip_input)
        elif user_input == "3":
            print("hydra")
        elif user_input == "4":
            print("burpsuite")
        elif user_input == "5":
            ip_input = input("Enter IP: ")
            dirbuster(ip_input)
        else:
            print("Please enter a valid option.")

        choice = input("Do you want to continue? (y/n): ").lower()
        if choice != 'y':
            break

if __name__ == "__main__":
    main()