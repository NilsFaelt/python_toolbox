#!/usr/bin/env python3

import subprocess

def nmap(ip):
    command = f"sudo nmap -oN ~/Desktop/scan_result {ip}"
    subprocess.run(command, shell=True)
    print("Nmap scan completed")

if __name__ == "__main__":
    target_ip = input("Enter the target IP address or range: ")
    nmap(target_ip)

