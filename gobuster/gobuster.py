"""Gobuster"""
import subprocess
import logging
import config
from util_functions.create_scan_results_path_and_dir import create_scan_results_path_and_dir


def gobuster(ip):
    """Quick scan gobuster"""
    try:
        scan_result_path = create_scan_results_path_and_dir()
        command = f"gobuster dir -u http://{ip} -w /usr/share/wordlists/rockyou.txt -o {scan_result_path}scan_result_gobuster.txt"
        subprocess.run(command, shell=True, check=True)
        print(f"DirBuster scan completed. Results saved to scan_result_dirb.txt on {config.dir_saved_scan_result}.")
    except subprocess.CalledProcessError as e:
        logging.error("Error occurred during command execution.")
        logging.error("Command: %s", e.cmd)
        logging.error("Return Code: %s", e.returncode)
        logging.error("Output: %s", e.output.decode("utf-8"))
