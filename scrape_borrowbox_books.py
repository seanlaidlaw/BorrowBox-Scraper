#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
import pickle

# Setup Chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_experimental_option("detach", True)

# Set path to chromedriver as per your configuration
webdriver_service = Service(ChromeDriverManager().install())

# Choose Chrome Browser
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

driver.get('https://hampshire.borrowbox.com/login')

# Assuming username field has id 'username' and password field has id 'password'
username = driver.find_element(By.ID, 'form-input-1')
password = driver.find_element(By.ID, 'form-input-2')

# Replace 'your_username' and 'your_password' with your actual username and password
username.send_keys('<Library Card Number>')
password.send_keys('<Pass Code>')

# Assuming login button has id 'login'
login_button = driver.find_element(By.XPATH, '//button[@type="submit" and contains(@class, "signin-button")]')
login_button.click()

# Wait for page to load
time.sleep(5)

# Save cookies
pickle.dump(driver.get_cookies() , open("cookies.pkl","wb"))

# Load cookies
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)

# Navigate to My Loans page
driver.get('https://hampshire.borrowbox.com/home/my-loans') # Replace with actual My Loans URL
time.sleep(5)


# Get all download buttons
download_buttons = driver.find_elements(By.CLASS_NAME, 'button-download')
nb_downloads = len(download_buttons)
print(download_buttons)

# Loop over download buttons
for i in range(nb_downloads):
    driver.get('https://hampshire.borrowbox.com/home/my-loans')
    time.sleep(5)

    # Click download button
    download_buttons = driver.find_elements(By.CLASS_NAME, 'button-download')
    button = download_buttons[i]
    button.click()

    # Wait for page to load
    time.sleep(5)

    # Find and click the "progress-button"
    progress_button = driver.find_element(By.CLASS_NAME, 'download-button')
    progress_button.click()
    time.sleep(60)

    driver.get('https://hampshire.borrowbox.com/home/my-loans')
    time.sleep(5)

# quit the chrome driver now books are downloaded
driver.quit()

