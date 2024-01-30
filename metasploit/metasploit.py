"""Starting metasploit"""
import subprocess
import logging

def metasploit():
    """Starting metasploit"""
    try:
        subprocess.run("msfconsole", shell=True , check=True)
        print("Metasploit finished")
    except subprocess.CalledProcessError as e:
        logging.error("Error occurred during command execution: %s", e)

if __name__ == "__main__":
    metasploit()
