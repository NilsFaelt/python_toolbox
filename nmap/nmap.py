import os
import config
import subprocess

def nmap(ip):
    scan_result_path = os.path.expanduser(f"{config.path_saved_scan_result}/scan_results/")  # Define the directory path
    os.makedirs(scan_result_path, exist_ok=True)  # Create the directory if it doesn't exist

    command = f"nmap -sV -p- >> {scan_result_path}scan_result_nmap.txt {ip}"
    subprocess.run(command, shell=True)
    print(f"Nmap scan completed, scan report saved to {scan_result_path} as scan_result")

if __name__ == "__main__":
    target_ip = input("enter the target IP address : ")
    nmap(target_ip)