import subprocess
def packages_and_info():
    print("Choose a package for info:")
    print("1. Nmap")
    print("2. SQLMap")
    print("3. Metasploit Framework")
    print("4. Wireshark")
    print("5. John the Ripper")
    print("6. Hydra")
    print("7. Aircrack-ng")
    print("8. Maltego")
    print("9. Nikto")
    print("10. WPScan")
    print("11. Burp Suite")
    print("12. Hashcat")
    print("13. Gobuster")
    print("14. Dirb")
    print("15. Volatility")

    choice = input("Enter the number of the package: ")

    if choice == "1":
        print("Nmap: Network Mapper - a powerful open-source network scanner used for network discovery and security auditing.")
    elif choice == "2":
        print("SQLMap: A tool used for automated SQL injection and database takeover.")
    elif choice == "3":
        print("Metasploit Framework: An advanced open-source penetration testing framework used for developing, testing, and executing exploits.")
    elif choice == "4":
        print("Wireshark: A network protocol analyzer used for capturing and analyzing packets in real-time.")
    elif choice == "5":
        print("John the Ripper: A popular password-cracking tool used to perform dictionary attacks against various types of encrypted passwords.")
    elif choice == "6":
        print("Hydra: A parallelized login cracker that supports numerous protocols for brute-forcing login credentials.")
    elif choice == "7":
        print("Aircrack-ng: A suite of tools used for assessing Wi-Fi network security, including packet sniffing, testing, and cracking WEP and WPA/WPA2-PSK encryption.")
    elif choice == "8":
        print("Maltego: A graphical link analysis tool used for gathering and connecting information for investigative tasks.")
    elif choice == "9":
        print("Nikto: An open-source web server scanner that performs comprehensive tests against web servers for multiple vulnerabilities.")
    elif choice == "10":
        print("WPScan: A black-box WordPress vulnerability scanner used to detect security issues within WordPress websites.")
    elif choice == "11":
        print("Burp Suite: A comprehensive web application security testing solution that includes various tools for security testing, scanning, and attacks.")
    elif choice == "12":
        print("Hashcat: An advanced password recovery tool used to crack hashed passwords.")
    elif choice == "13":
        print("Gobuster: A directory and file brute-forcing tool used to discover hidden content on web servers.")
    elif choice == "14":
        print("Dirb: A web content scanner used for discovering hidden directories and files on web servers.")
    elif choice == "15":
        print("Volatility: An advanced memory forensics framework used for analyzing volatile memory dumps for malware analysis and incident response.")
    else:
        print("Invalid choice. Please enter a valid number corresponding to the package.")


if __name__ == "__main__":
    packages_and_info()
