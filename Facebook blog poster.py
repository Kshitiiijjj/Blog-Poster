from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Firefox driver
driver = webdriver.Firefox()

# Open Facebook login page
driver.get('https://www.facebook.com/')

# Wait for the email input and enter email
email_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="email"]'))
)
email_element.send_keys('test@gmail.com')

# Wait for the password input and enter password
pass_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="pass"]'))
)
pass_element.send_keys('test@1234')

# Wait for the login button and click it
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@name="login"]'))
)
login_button.click()

# Wait for the page to load after login
time.sleep(5)  # You can adjust this time as needed

# Use the provided XPath for the status input
status_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div"))
)
status_element.send_keys('Hi there')

# Wait for the Post button to be clickable and click it
post_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div/div/div[1]"))
)
post_button.click()

# Close the driver
driver.quit()