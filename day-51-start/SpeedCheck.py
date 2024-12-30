import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException

Method1_LINK = "https://www.speedtest.net/"
Method2_LINK = "https://fast.com/"

class InternetSpeedTwitterBot:
    def __init__(self, username, password):
        self.driver = None
        self.web_wait = None

        self.username = username
        self.password = password

        self.tries = 0
        self.up = "Not given"
        self.down = "Not given"
    def initialize_driver(self):
        """Initialize the WebDriver."""
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(option)
        self.web_wait = WebDriverWait(self.driver, 10)

    def get_internet_speed(self):
        if self.tries == 5:
            return "Too many tries, please try again latter."
        user_prompt = input("Which method do you want to use. Method 1 / Method 2: ").lower()

        def get_down_up():
            ## get down and up data and returns fetched data to method 1
            try:
                time.sleep(10)  # Simulating delay
                down = self.web_wait.until(EC.visibility_of_element_located(
                    (By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')))
                up = self.web_wait.until(EC.visibility_of_element_located(
                    (By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')))
                print(f"Down: {down.text}, Up: {up.text}")
                try:
                    result_down= float(down.text)
                    result_up = float(up.text)
                    self.down = result_down
                    self.up = result_up
                except ValueError:
                    get_down_up()
            except TimeoutException:
                return "Try again"
            return "Data fetched successfully"
        def method1():
            """Method 1 return both up and down speed test, but it takes more time. Around 1~2 minutes. Source 'www.speedtest.net'"""
            self.initialize_driver()
            self.driver.get(Method1_LINK)
            try:
                start = self.web_wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "start-text")))
                print("clicked once")
            except TimeoutException:
                print("an able to click retrying")
                time.sleep(2)
                start = self.web_wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "start-text")))
                print("clicked successfully")
            start.click()

            tries = 0
            max_tries = 5

            while tries < max_tries:
                result = get_down_up()  # Store the result once
                if result == "Try again":
                    tries += 1
                    print(f"Attempt {tries} failed. Retrying...")
                elif result == "Data fetched successfully":
                    print("Data fetched successfully:")
                    return result
                else:
                    print("Unexpected result:", result)
            else:
                print("Couldn't fetch data after maximum retries. Please try again.")



        def method2():
            """Method 2 return single download speed, and it is much faster compared to Method 1. Source 'fast.com'."""
            self.initialize_driver()
            self.driver.get(Method2_LINK)
            time.sleep(3)
            try:
                down_speed_result = self.web_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".speed-results-container.succeeded")))
            except TimeoutException:
                down_speed_result = self.web_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".speed-results-container.succeeded")))

            print(down_speed_result.text)
            result = down_speed_result.text
            self.down = float(result)
            self.up = "Not given"

        if user_prompt == "method 1":
            self.tries = 0
            method1()
            self.driver.quit()

        elif user_prompt == "method 2":
            self.tries = 0
            method2()
            self.driver.quit()
        else:
            self.tries += 1
            print("Invalid Input. Please try again")
            self.get_internet_speed()
    def tweet_at_provider(self):
        self.initialize_driver()
        self.driver.get('https://x.com/home?lang=en')
        sign_in = self.web_wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[4]/a')))
        sign_in.click()

        ## login in process
        time.sleep(2)
        user_input = self.web_wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')))
        user_input.send_keys(self.username, Keys.ENTER)

        time.sleep(2)
        password_input = self.web_wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')))
        password_input.send_keys(self.password, Keys.ENTER)
        print("Registered to Twitter successfully")
        ### write a post
        time.sleep(3)
        post = self.web_wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')))
        post.send_keys(f"Hello! I am practicing Python. This is auto bot posting my internet download and upload speed.\nDownload: {self.down}\nUpload: {self.up}")

        ### post result
        result_post = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        result_post.click()
        print("Internet speed details posted successfully")