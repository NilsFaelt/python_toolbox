"""Starting wpscan"""
import subprocess
import config
from util_functions.create_scan_results_path_and_dir import create_scan_results_path_and_dir

def wpscan(ip):
    """Starting wpscan"""
    try:
        scan_result_path = create_scan_results_path_and_dir()
        command = f"wpscan --url https://{ip} --enumerate vp >> {scan_result_path}/scan_result_wpscan.txt"
        subprocess.run(command, shell=True, check=True)
        print(f"WPScan scan completed. Results saved to scan_result_wpscan.txt in {config.dir_saved_scan_result}.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    target_ip = input("enter the target IP address : ")
    wpscan(target_ip) 
