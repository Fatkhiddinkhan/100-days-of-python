from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=option)
driver.get("https://www.python.org/")

date = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/time')
events = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/a')


formate = {}
num = 0
for single_date, event in zip(date, events):
    formate[num] = {
        "time": single_date.text,
        "name": event.text
    }
    num += 1
print(formate)
driver.quit()