import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By


def spy_photo(url):
    """Taking screenshots with selenium"""
    print('selenium')
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    if not url:
        website_url = 'https://unsplash.com'
    else:
        website_url = url    
    driver.get(website_url)
    time.sleep(1)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_name = f"./spy_shots/screenshot_{timestamp}.png"
    driver.save_screenshot(screenshot_name)
    driver.execute_script("window.scrollBy(0, window.innerHeight);") 
    time.sleep(1)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_name = f"./spy_shots/screenshot_{timestamp}_after_scroll.png"
    driver.save_screenshot(screenshot_name)
    driver.execute_script("window.scrollBy(0, window.innerHeight);") 
    time.sleep(1)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_name = f"./spy_shots/screenshot_{timestamp}_after_scroll.png"
    driver.save_screenshot(screenshot_name)
    driver.quit()





