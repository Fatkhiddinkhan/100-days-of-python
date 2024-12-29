import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

GOOGLE_ACOUNT = input("Enter your google account: ")
GOOGLE_PASSWORD = input("Enter your google password: ")

## keep the web opened
web_options = webdriver.ChromeOptions()
web_options.add_experimental_option('detach', True)

## create driver
driver = webdriver.Chrome(options=web_options)
driver.get("https://tinder.com/")

## set waits, web_wait = 5 seconds, long_wait = 15seconds
web_wait = WebDriverWait(driver, 5)
long_wait = WebDriverWait(driver, 10)


### login in process
login_in = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login_in.click()
print('Login in button found successfully')

google_reg = web_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'iframe[title="Google 계정으로 로그인 버튼"]')))
google_reg.click()
print("\nGoogle registration method found")

base_window = driver.window_handles[0]

google_login_window = driver.window_handles[1]

driver.switch_to.window(google_login_window)
print("driver switched successfully")
print(driver.title)

google_email_input = web_wait.until(EC.visibility_of_element_located((By.ID, 'identifierId')))
google_email_input.send_keys(GOOGLE_ACOUNT, Keys.ENTER)
print("Email entered successfully")

google_password_input = web_wait.until(EC.visibility_of_element_located((By.NAME, 'Passwd')))
google_password_input.send_keys(GOOGLE_PASSWORD, Keys.ENTER)
print("Password entered successfully")
driver.switch_to.window(base_window)
try:
    location_allow = web_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Allow"]')))
    print("\nSucceeded")
except TimeoutException:
    print('\nSearching by css selector failed')
    location_allow = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]')

location_allow.click()

try:
    notification = web_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[aria-label="I’ll miss out"]')))
    print("Succeeded")
except TimeoutException:
    print('\nSearching by css selector failed')
    notification = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[3]/button[2]')

notification.click()
print("Bot set successfully")

cookie = long_wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button')))
cookie.click()
print("Accepted all cookie")
like_button = long_wait.until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[4]/div/div[4]/button')))
like_button.click()
print('liked')
for _ in range(100):
    time.sleep(2)
    try:
        print('1')
        like = web_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button span span[class="gamepad-icon-wrapper"]')))
    except TimeoutException:
        print('2')
        like = driver.find_element(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[5]/div/div[4]/button/span/span[1]')))
    like.click()
    print("liked successfully")

