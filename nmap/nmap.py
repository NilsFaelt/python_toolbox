import os
import config
import subprocess
import create_scan_results_path_and_dir from create_scan_results_path_and_dir
import logging

def nmap(ip):
    try:
        scan_result_path = create_scan_results_path_and_dir()

        command = f"nmap -sV -p- >> {scan_result_path}scan_result_nmap.txt {ip}"
        subprocess.run(command, shell=True)
        print(f"Nmap scan completed, scan report saved to {scan_result_path} as scan_result")
    except Exception as e:
        logging.error(f"An error occurred during Nmap scan: {e}")

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    nmap(target_ip)
