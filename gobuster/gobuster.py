import subprocess
import config

def gobuster(ip):
    try:
        command = f"gobuster dir -u http://{ip} -w /path/to/wordlist.txt -o {config.path_saved_scan_resul}scan_result_gobuster.txt"
        subprocess.run(command, shell=True)
        print(f"DirBuster scan completed. Results saved to scan_result_dirb.txt on {config.dir_saved_scan_resul}.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    gobuster(ip_address)


