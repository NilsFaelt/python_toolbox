import config
import subprocess

def wpscan(ip):
    try:
        print(config.path_saved_scan_result)
        command = f"wpscan --url https://{ip} --enumerate vp >> {config.path_saved_scan_result}scan_result_wpscan.txt"
        subprocess.run(command, shell=True)
        print("WPScan scan completed. Results saved to scan_result_wpscan.txt on Desktop.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    target_ip = input("enter the target IP address : ")
    wpscan(target_ip) 
