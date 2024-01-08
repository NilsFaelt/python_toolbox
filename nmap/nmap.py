#!/usr/bin/env python3
import config
import subprocess


def nmap(ip):
    command = f"nmap -sV -p- -oN {config.path_saved_scan_result}scan_result_nmap.txt {ip}"
    subprocess.run(command, shell=True)
    print("Nmap scan completed, scan report saved to home as scan_result")

if __name__ == "__main__":
    target_ip = input("enter the target IP address : ")
    nmap(target_ip)

