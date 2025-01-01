import time
from itertools import zip_longest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import TimeoutException, StaleElementReferenceException, ElementNotInteractableException

LINK = "https://forms.gle/TGfxxMRNuhjGs4Q58"
class GoogleSheetBot:
    def __init__(self):
        self.address = None
        self.price  = None
        self.link = None

        self.driver = None
        self.web_wait = None
    def receive_data(self, address, price, link):
        self.address = address
        self.price  = price
        self.link = link
        if len(self.address) > 1 and len(self.price) > 1 and len(self.link) > 1:
            print("Data received successfully.")

        else:
            print("There is no data.")

    def run_bot(self):
        print("Running driver")
        web_option = webdriver.ChromeOptions()
        web_option.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(web_option)
        self.driver.get(LINK)

        self.web_wait = WebDriverWait(self.driver, 5)
        print("Your Bot initialized and ready.")
        self.fill_blanks()
    def fill_blanks(self):
        n = 1
        for address, price, link in zip_longest(self.address, self.price, self.link, fillvalue="Not Given"):
            try:
                blank1 = self.web_wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                         '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
                blank1.send_keys(address, Keys.ENTER)

                blank2 = self.web_wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                         '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
                blank2.send_keys(price, Keys.ENTER)

                blank3 = self.web_wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                         '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
                blank3.send_keys(link, Keys.ENTER)

                submit = self.driver.find_element(By.XPATH,
                                                  '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
                submit.click()

                new_submit = self.web_wait.until(
                    EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')))
                new_submit.click()

                if n == len(self.link):
                    print("All properties submitted with link, price and address.")
                else:
                    print(f"Submitted {n} out of {len(self.link)}")
                n += 1
            except ElementNotInteractableException:
                print("Sorry cannot interact with input")
                continue





