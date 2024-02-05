import time
from datetime import datetime
from selenium import webdriver


def spy_photo():
    """Taking screenshots with selenium"""
    print('selenium')
    chrome_options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(options=chrome_options)
    
    website_url = 'https://unsplash.com'
    driver.get(website_url)
    
    time.sleep(2)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_name = f"./spy_shots/screenshot_{timestamp}.png"
    driver.save_screenshot(screenshot_name)
    driver.execute_script("window.scrollBy(0, window.innerHeight);") 
    time.sleep(2)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_name = f"./spy_shots/screenshot_{timestamp}_after_scroll.png"
    driver.save_screenshot(screenshot_name)
    driver.execute_script("window.scrollBy(0, window.innerHeight);") 
    time.sleep(2)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_name = f"./spy_shots/screenshot_{timestamp}_after_scroll.png"
    driver.save_screenshot(screenshot_name)
    driver.quit()

if __name__ == "__main__":
    spy_photo()



