import os
import config
import subprocess
import logging

def nmap(ip):
    try:
        scan_result_path = os.path.expanduser(f"{config.path_saved_scan_result}/scan_results/")
        os.makedirs(scan_result_path, exist_ok=True)

        command = f"nmap -sV -p- >> {scan_result_path}scan_result_nmap.txt {ip}"
        subprocess.run(command, shell=True)
        print(f"Nmap scan completed, scan report saved to {scan_result_path} as scan_result")
    except Exception as e:
        logging.error(f"An error occurred during Nmap scan: {e}")

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    nmap(target_ip)
