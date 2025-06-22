
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to the Demo Web Shop login page
driver.get("https://demowebshop.tricentis.com/login")

# Input login credentials
driver.find_element(By.ID, "Email").send_keys("your_email@example.com")
driver.find_element(By.ID, "Password").send_keys("your_password")

# Click the Login button
driver.find_element(By.CSS_SELECTOR, "input.login-button").click()

# Wait for page to load and capture a screenshot
time.sleep(3)
driver.save_screenshot("login_result.png")

# Close the browser
driver.quit()
