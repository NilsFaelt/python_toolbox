import subprocess

def update_packages():
    """Updateing packages"""
    try:
        subprocess.run(["apt-get", "update"], check=True)
        subprocess.run(["apt-get", "upgrade", "-y"],check=True)
        subprocess.run(["apt-get", "install", "nmap", "-y"],check=True)
        subprocess.run(["apt-get", "install", "sqlmap", "-y"],check=True)
        subprocess.run(["apt-get", "install", "metasploit-framework", "-y"],check=True)
        subprocess.run(["apt-get", "install", "wireshark", "-y"],check=True)
        subprocess.run(["apt-get", "install", "john", "-y"],check=True)
        subprocess.run(["apt-get", "install", "hydra", "-y"],check=True)
        subprocess.run(["apt-get", "install", "aircrack-ng", "-y"],check=True)
        subprocess.run(["apt-get", "install", "maltego", "-y"],check=True)
        subprocess.run(["apt-get", "install", "nikto", "-y"],check=True)
        subprocess.run(["apt-get", "install", "wpscan", "-y"],check=True)
        subprocess.run(["apt-get", "install", "burpsuite", "-y"],check=True)
        subprocess.run(["apt-get", "install", "hashcat", "-y"],check=True)
        subprocess.run(["apt-get", "install", "gobuster", "-y"],check=True)
        subprocess.run(["apt-get", "install", "dirb", "-y"],check=True)
        subprocess.run(["apt", "install", "curl", "-y"],check=True)
        subprocess.run(["apt", "install", "wordlists"],check=True)
        subprocess.run(["gunzip", "/usr/share/wordlists/rockyou.txt.gz"],check=True)
           
        print("Packages updated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    update_packages()
