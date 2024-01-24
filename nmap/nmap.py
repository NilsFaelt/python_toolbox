"""Nmap"""
import subprocess
import logging
from util_functions.create_scan_results_path_and_dir import create_scan_results_path_and_dir

def nmap(ip):
    """Nmap preset scan for starting a scan"""
    try:
        scan_result_path = create_scan_results_path_and_dir()
        command = f"nmap -sV -p- >> {scan_result_path}scan_result_nmap.txt {ip}"
        subprocess.run(command, shell=True, check=True)
        print(f"Nmap scan completed, scan report saved to {scan_result_path} as scan_result")
    except subprocess.CalledProcessError as e:
        logging.error("Error occurred during command execution.")
        logging.error("Command: %s", e.cmd)
        logging.error("Return Code: %s", e.returncode)
        logging.error("Output: %s", e.output.decode("utf-8"))

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    nmap(target_ip)
