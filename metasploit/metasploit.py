import subprocess

def metasploit():
    try:
        subprocess.run("msfconsole", shell=True)
        print("Metasploit finished")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    metasploit()
