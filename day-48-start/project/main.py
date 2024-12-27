from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from time import time

# Website link
COOKIE_CLICKER_URL = "https://orteil.dashnet.org/experiments/cookie/"

# Keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize driver
driver = webdriver.Chrome(options=chrome_options)
driver.get(COOKIE_CLICKER_URL)

# Get the clickable cookie element
cookie_button = driver.find_element(By.ID, "cookie")

# Get store items and extract their IDs
store_items = driver.find_elements(By.CSS_SELECTOR, "div#store div")
store_item_ids = [item.get_attribute("id") for item in store_items]

# Create a list of prices (as text) for each store item
store_item_texts = [
    driver.find_element(By.ID, store_item_ids[i]).text.split('\n')[0]
    for i in range(len(store_item_ids))
]

# From each store item text, extract the numeric part
store_item_cost_strings = [
    text.split(" - ")[1] for text in store_item_texts if len(text) > 1
]

# Start timers
purchase_check_time = time()  # Timer for 5 seconds
script_start_time = time()    # Timer for 300 seconds


if_looped = 0
while True:
    if_looped += 1
    # Click the cookie to earn money
    cookie_button.click()

    # Get the current amount of money
    money_text = driver.find_element(By.ID, "money").text
    if "," in money_text:
        current_money = int(money_text.replace(",", ""))
    else:
        current_money = int(money_text)

    # Build a dictionary from item_id as a key, item_cost (as int) as a value
    item_cost_dict = {}
    # Iterate backwards so we always check the most expensive item first
    for idx in range(len(store_item_cost_strings) - 1, -1, -1):
        cost_str = store_item_cost_strings[idx].replace(",", "")
        item_cost_dict[store_item_ids[idx]] = int(cost_str)

    # Every 5 seconds, check if we can buy something
    if time() - purchase_check_time > 5:
        purchase_check_time = time()

        # Try to buy from the most expensive item down to the cheapest
        for item_id, item_cost in item_cost_dict.items():
            if current_money >= item_cost:
                try:
                    driver.find_element(By.ID, item_id).click()
                    print(f"Purchased {item_id} for {item_cost} cookies.")
                except StaleElementReferenceException:
                    # If the element becomes stale, skip it
                    pass
                break  # After a successful purchase, break to re-check money next time

    # End script after 300 seconds
    if time() - script_start_time > 300:
        break
print(driver.find_element(By.ID, "cps").text)
driver.quit()