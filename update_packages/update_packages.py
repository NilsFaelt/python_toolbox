import subprocess
import config
import os

def update_packages():
    try:
        scan_results_dir = os.path.join(config.path_saved_scan_result, 'scan_results')
        os.makedirs(scan_results_dir, exist_ok=True)
        subprocess.run(["apt-get", "update"])
        subprocess.run(["apt-get", "upgrade", "-y"])
        subprocess.run(["apt-get", "install", "nmap", "-y"])
        subprocess.run(["apt-get", "install", "sqlmap", "-y"])
        subprocess.run(["apt-get", "install", "metasploit-framework", "-y"]) 
        subprocess.run(["apt-get", "install", "wireshark", "-y"]) 
        subprocess.run(["apt-get", "install", "john", "-y"]) 
        subprocess.run(["apt-get", "install", "hydra", "-y"]) 
        subprocess.run(["apt-get", "install", "aircrack-ng", "-y"]) 
        subprocess.run(["apt-get", "install", "maltego", "-y"]) 
        subprocess.run(["apt-get", "install", "nikto", "-y"]) 
        subprocess.run(["apt-get", "install", "wpscan", "-y"]) 
        subprocess.run(["apt-get", "install", "burpsuite", "-y"]) 
        subprocess.run(["apt-get", "install", "hashcat", "-y"])  
        subprocess.run(["apt-get", "install", "gobuster", "-y"]) 
        subprocess.run(["apt-get", "install", "dirb", "-y"])  
        subprocess.run(["apt-get", "install", "volatility", "-y"]) 
        
        
        print("Packages updated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    update_packages()
