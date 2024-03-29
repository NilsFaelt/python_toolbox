"""Scaning website with curl"""
import re
import subprocess

def scan_curl_for_users(url):
    """Scaning website with curl"""
    print(url)
    try:
        response = subprocess.check_output(['curl', url], text=True, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f"Error running curl: {e.stderr}")
        return []

    words = re.findall(r'\b\w+@[\w.-]+\b', response)
    unique_words = list(set(words))
    print(unique_words)
    return unique_words