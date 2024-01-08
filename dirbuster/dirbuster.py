import subprocess

def dirbuster(ip):
    try:
        command = f"gobuster dir -u http://{ip} -w /path/to/wordlist.txt -o ~/Desktop/scan_result_gobuster.txt"
        subprocess.run(command, shell=True)
        print("DirBuster scan completed. Results saved to scan_result_dirb.txt on Desktop.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_dirbuster(ip_address)


