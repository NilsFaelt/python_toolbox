#!/usr/bin/env python3

import subprocess

def nmap(ip):
    command = f"nmap -oN ../scan_results/scan_result {ip}"
    subprocess.run(command, shell=True)
    print("Nmap scan completed, scan saved to directory scan_results, inside python_toolbox directory ")

if __name__ == "__main__":
    target_ip = input("enter the target IP address or range: ")
    nmap(target_ip)

