import subprocess

def update_packages():
    try:
        subprocess.run(["apt-get", "update"], check=False)
        subprocess.run(["apt-get", "upgrade", "-y"],check=False)
        subprocess.run(["apt-get", "install", "nmap", "-y"],check=False)
        subprocess.run(["apt-get", "install", "sqlmap", "-y"],check=False)
        subprocess.run(["apt-get", "install", "metasploit-framework", "-y"],check=False)
        subprocess.run(["apt-get", "install", "wireshark", "-y"],check=False)
        subprocess.run(["apt-get", "install", "john", "-y"],check=False)
        subprocess.run(["apt-get", "install", "hydra", "-y"],check=False)
        subprocess.run(["apt-get", "install", "aircrack-ng", "-y"],check=False)
        subprocess.run(["apt-get", "install", "maltego", "-y"],check=False)
        subprocess.run(["apt-get", "install", "nikto", "-y"],check=False)
        subprocess.run(["apt-get", "install", "wpscan", "-y"],check=False)
        subprocess.run(["apt-get", "install", "burpsuite", "-y"],check=False)
        subprocess.run(["apt-get", "install", "hashcat", "-y"],check=False)
        subprocess.run(["apt-get", "install", "gobuster", "-y"],check=False)
        subprocess.run(["apt-get", "install", "dirb", "-y"],check=False)
        subprocess.run(["apt-get", "install", "volatility", "-y"],check=False)
        subprocess.run(["apt", "install", "curl", "-y"],check=False)
        subprocess.run(["apt", "install", "wordlists", "-y"],check=False)
        subprocess.run(["gunzip", "/usr/share/wordlists/rockyou.txt.gz"],check=False)
        
        
        print("Packages updated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    update_packages()
