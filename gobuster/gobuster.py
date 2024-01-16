"""Gobuster"""
import subprocess
import config
from util_functions.create_scan_results_path_and_dir import create_scan_results_path_and_dir


def gobuster(ip):
    """Quick scan gobuster"""
    try:
        scan_result_path = create_scan_results_path_and_dir()
        command = f"gobuster dir -u http://{ip} -w /path/to/wordlist.txt -o {scan_result_path}scan_result_gobuster.txt"
        subprocess.run(command, shell=True)
        print(f"DirBuster scan completed. Results saved to scan_result_dirb.txt on {config.dir_saved_scan_result}.")
    except Exception as e:
        print(f"An error occurred: {e}")

