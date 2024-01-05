import subprocess

def update_packages():
    try:
        subprocess.run(["sudo", "apt-get", "update"])
        subprocess.run(["sudo", "apt-get", "upgrade", "-y"])
        subprocess.run(["sudo", "apt-get", "install", "nmap", "-y"])
        
        print("Packages updated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    update_packages()
