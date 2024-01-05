#!/usr/bin/env python3

import subprocess

def nmap(ip): 
    home_directory = os.path.expanduser("~")
    scan_result_path = os.path.join(home_directory, "scan_result.txt")
    command = f"nmap -oN {scan_result_path} {ip}"
    os.system(command)

if __name__ == "__main__":
    target_ip = input("enter the target IP address or range: ")
    nmap(target_ip)

