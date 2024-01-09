from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver_path = '/usr/bin/chromedriver' # Replace with your chromedriver location
url = 'https://old.reddit.com/user/YourUsername/comments/' # Replace with your username

reddit_username = 'YourUsername'  # Replace with your username
reddit_password = 'YourPassword'  # Replace with your password

from selenium.webdriver.chrome.service import Service
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get(url)
time.sleep(2)

login_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'login-link')]"))
)
login_link.click()
time.sleep(5)

username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user_login")))
username_field.send_keys(reddit_username)

password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "passwd_login")))
password_field.send_keys(reddit_password)

login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/form/div[5]/button"))
)
login_button.click()

time.sleep(10)

div_index = 1

while True:
    try:
        delete_xpath = f"/html/body/div[3]/div[2]/div[{div_index}]/div[2]/ul/li[7]/form/span[1]/a"
        delete_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, delete_xpath))
        )
        delete_link.click()
        time.sleep(0.5)

        yes_xpath = f"/html/body/div[3]/div[2]/div[{div_index}]/div[2]/ul/li[7]/form/span[2]/a[1]"
        yes_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, yes_xpath))
        )
        yes_link.click()
        time.sleep(0.5)

        div_index += 2

    except Exception as e:
        print(f"Attempting to refresh: {e}")
        driver.refresh()
        time.sleep(0.5)
        div_index = 1

driver.quit()
