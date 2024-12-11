from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Constants for Tinder login
EMAIL = "your_email@example.com"
PASSWORD = "your_password"

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open Tinder login page
driver.get("https://tinder.com")

# Wait for the page to load
time.sleep(5)

# Click on the login button
login_button = driver.find_element(By.XPATH, '//*[@id="t-123456789"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
login_button.click()

# Wait for the login options to appear
time.sleep(2)

# Select login with Facebook
facebook_login = driver.find_element(By.XPATH, '//*[@id="t-123456789"]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook_login.click()

# Switch to Facebook login window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

# Enter email and password for Facebook login
email_input = driver.find_element(By.ID, "email")
email_input.send_keys(EMAIL)
password_input = driver.find_element(By.ID, "pass")
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.ENTER)

# Switch back to Tinder window
driver.switch_to.window(base_window)

# Wait for Tinder to load
time.sleep(5)

# Allow location access
allow_location_button = driver.find_element(By.XPATH, '//*[@id="t-123456789"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

# Allow notifications
allow_notifications_button = driver.find_element(By.XPATH, '//*[@id="t-123456789"]/div/div/div/div/div[3]/button[2]')
allow_notifications_button.click()

# Start swiping right
for _ in range(100):
    time.sleep(1)
    try:
        like_button = driver.find_element(By.XPATH, '//*[@id="t-123456789"]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(2)

# Close the driver
driver.quit()
