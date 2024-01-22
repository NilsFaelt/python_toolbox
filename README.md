# Pentesting Toolbox Automation

## Description
A Python project aiming to automate the usage of various penetration testing (pentesting) tools. This toolbox will streamline and facilitate the execution of common pentesting tasks.

## Technologies Used
- Python
- bash
- vim

## Getting Started
To use this toolbox, follow these steps:

### Setting up Kali Linux Rolling
1. Install Docker on your machine if not already installed. You can download Docker Desktop from the official website based on your operating system.
2. Pull the Kali Linux Rolling Docker image:
    ```bash
    docker pull kalilinux/kali-rolling
    ```

### Installing Python 3 in the Kali Linux container
1. Run the Kali Linux container and access it:
    ```bash
    docker run -it kalilinux/kali-rolling /bin/bash
    ```
2. Update the package lists and install Python 3:
    ```bash
    apt-get update
    apt-get install -y python3
    apt-get install git
    apt-get install pip
    ```

### Cloning and Running the Python Code
3. Clone this repo
    ```bash
    git clone https://github.com/NilsFaelt/python_toolbox.git
    ```
4. Navigate to the project directory and execute your Python code:
    ```bash
    cd python_toolbox
    pip install -r requirements.txt
    ```
    ```
5. Inside project run Pip:
   ```bash
    python3 main.py
    ```
6. Choose option 1 first time you use toolbox to install tools
    ```bash
    choose option 1 inside toolbox
    ```

### This toolbox is only for legal purposes
  Dont use any of theese tools if you dont have authority to do so.
  Do not test any of theese tools on any website or server were, were you are not authorised to do so.
