from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options

LINK = "https://secure-retreat-92358.herokuapp.com/"

# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Enable headless mode
# chrome_options.add_argument("--disable-gpu")  # Disable GPU (optional)
# chrome_options.add_argument("--window-size=1920x1080")  # Optional, sets the window size for rendering

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option)
driver.get(LINK)

# num_articles = driver.find_element(By.CSS_SELECTOR, value="div#articlecount a").text
# num_articles.click()

# click_on = driver.find_element(By.LINK_TEXT, value=num_articles)
# driver.quit()

## type and click

# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Fatkhiddin", Keys.ENTER)

## challenge sign in to web page

fname = driver.find_element(By.NAME, value="fName")
fname.send_keys("Fatkhiddin", Keys.ENTER)
lname = driver.find_element(By.NAME, value="lName")
lname.send_keys("Numonov", Keys.ENTER)
email = driver.find_element(By.NAME, value="email")
email.send_keys("Fatkhiddin@gmail.com", Keys.ENTER)

