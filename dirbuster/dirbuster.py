import subprocess

def dirbuster(ip):
    try:
        command = f"dirb http://{ip} -o ~/Desktop/scan_result_dirb.txt"
        subprocess.run(command, shell=True)
        print("DirBuster scan completed. Results saved to scan_result_dirb.txt on Desktop.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_dirbuster(ip_address)


