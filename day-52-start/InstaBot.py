import os
import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import TimeoutException, StaleElementReferenceException

INSTA_URL = "https://www.instagram.com/"
INFO_PATH = "./info"

class InstaFollowersBot:
    def __init__(self, username, password, target_account):
        self.username = username
        self.password = password
        self.target_account = target_account

        # We'll store the total count of "people" (followers or following) in this variable.
        self.total_count = None

        # Shared list that gets filled each time we fetch followers or following.
        self.all_people_list = []

        self.driver = None
        self.web_wait = None

        # Keep a last-used random number to vary waits a bit.
        self.random_number = 0

    def get_random_delay(self):
        """Generate a small random integer (1-4) for sleeping, ensuring we don't repeat."""
        number = random.randint(1, 4)
        if self.random_number != number:
            self.random_number = number
            return number
        else:
            # If it's the same, pick again.
            return self.get_random_delay()

    def web_initialize(self):
        """Initialize the Chrome WebDriver with a small wait."""
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=options)
        self.web_wait = WebDriverWait(self.driver, 5)
        print("Web driver initialized and ready.")

    def insta_login(self):
        """Open Instagram and attempt to log in with provided credentials."""
        self.web_initialize()
        self.driver.get(INSTA_URL)

        # Sleep a random delay to mimic human behavior
        time.sleep(self.get_random_delay())

        # Enter username
        username_field = self.web_wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[aria-label="Phone number, username, or email"]'))
        )
        username_field.send_keys(self.username, Keys.ENTER)

        # Enter password
        password_field = self.web_wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[aria-label="Password"]'))
        )
        password_field.send_keys(self.password, Keys.ENTER)
        print("Login credentials submitted.")

        time.sleep(self.get_random_delay())
        self.info_check()

    def info_check(self):
        """
        Quickly checks whether Instagram threw an error about incorrect username/password.
        If not found, we assume login was successful.
        """
        attempts = 0
        while attempts < 2:
            try:
                # If this element is found, it means there's a login error
                self.web_wait.until(
                    EC.visibility_of_element_located((
                        By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/span/div'
                    ))
                )
                print("Sorry, your username or password was incorrect.")
                attempts += 1
            except TimeoutException:
                print("Successfully logged in.")
                break

    def fetch_full_info(self):
        """
        Convenience method to fetch both followers and following in one call.
        """
        self.fetch_followers()
        self.fetch_followings()

    def fetch_followers(self):
        """Go to the target account profile, click the followers count, fetch the list, then analyze."""
        time.sleep(self.get_random_delay())
        self.driver.get(f"{INSTA_URL}/{self.target_account}/")

        # Get total followers
        total_followers_el = self.web_wait.until(
            EC.visibility_of_element_located((
                By.XPATH,
                '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a/span/span'
            ))
        )
        # Try also to get total following (not necessarily used here, but can be displayed)
        total_following_el = self.web_wait.until(
            EC.visibility_of_element_located((
                By.XPATH,
                '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[3]/div/a/span/span'
            ))
        )

        # Convert followers to int. If Instagram uses "k"/",", this may break; handle that if needed.
        self.total_count = int(total_followers_el.text)
        print(
            f"Found target account: {self.target_account}\n"
            f"Followers: {total_followers_el.text}, Following: {total_following_el.text}"
        )

        time.sleep(self.get_random_delay())
        total_followers_el.click()

        # Clear out old list, then fetch
        self.all_people_list = []
        self.fetch_people_list("followers")
        self.analyze_list("followers")

    def fetch_followings(self):
        """Go to the target account profile, click the following count, fetch the list, then analyze."""
        time.sleep(self.get_random_delay())
        self.driver.get(f"{INSTA_URL}/{self.target_account}/")

        total_following_el = self.web_wait.until(
            EC.visibility_of_element_located((
                By.XPATH,
                '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[3]/div/a/span/span'
            ))
        )
        self.total_count = int(total_following_el.text)
        total_following_el.click()

        # Clear out old list, then fetch
        self.all_people_list = []
        self.fetch_people_list("followings")
        self.analyze_list("followings")

    def fetch_people_list(self, list_type):
        """
        Scrolls through the popup and grabs each username from the list of either followers or following.
        Uses absolute XPaths that might break if Instagram changes its layout.
        """
        print(f"Fetching {list_type}...")
        scroll_height = 70
        index_in_list = 1
        fetched_count = 1

        while fetched_count < self.total_count:
            fetched_count += 1
            try:
                # Locate the popup container
                popup = self.web_wait.until(
                    EC.visibility_of_element_located((
                        By.XPATH,
                        '/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]'
                    ))
                )

                # Locate a single item
                person_el = self.web_wait.until(
                    EC.visibility_of_element_located((
                        By.XPATH,
                        f'/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{index_in_list}]/div/div/div/div[2]/div/div/div/div/div/a/div/div/span'
                    ))
                )

                index_in_list += 1
                self.all_people_list.append(person_el.text)
                print(person_el.text)

                # Scroll down a bit
                self.driver.execute_script("arguments[0].scrollTop += arguments[1];", popup, scroll_height)

            except TimeoutException:
                print(f"Could not find {list_type} at index {index_in_list}. Retrying...")
                continue
            except StaleElementReferenceException:
                print("Popup became stale. Re-locating the popup...")
                # Re-find the popup and scroll again
                popup = self.web_wait.until(
                    EC.visibility_of_element_located((
                        By.XPATH,
                        '/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]'
                    ))
                )
                self.driver.execute_script("arguments[0].scrollTop += arguments[1];", popup, scroll_height)

        print(f"Finished fetching {list_type}. Total found: {len(self.all_people_list)}")

    def analyze_list(self, list_type):
        """
        Creates a folder for 'followers' or 'followings' inside ./info/{target_account},
        then checks for new and canceled (removed) people.
        """
        # We'll collect new people in this local list
        newly_found_list = []

        # Create the directory for this target and type
        account_dir = os.path.join(INFO_PATH, self.target_account, list_type)
        if not os.path.isdir(account_dir):
            os.makedirs(account_dir)
            print(f"Created folder: {account_dir}")
        else:
            print(f"Folder already exists: {account_dir}")

        def process_existing_people():
            """
            Check if there's a 'total_people' file with old data.
            If not, create it. If yes, append new entries and track them in newly_found_list.
            """
            file_path = os.path.join(account_dir, "total_people")
            try:
                with open(file_path, "r") as f:
                    old_people = [line.strip() for line in f]
            except FileNotFoundError:
                # If file doesn't exist, write all current people
                with open(file_path, "w") as f:
                    for person in self.all_people_list:
                        f.write(f"{person}\n")
                return

            # Append new people
            with open(file_path, "a") as f:
                for person in self.all_people_list:
                    if person not in old_people:
                        f.write(f"{person}\n")
                        newly_found_list.append(person)

        def record_new_people():
            """
            Appends newly found people to 'new_people.txt' (within account_dir).
            Avoids duplicates by checking existing content.
            """
            new_file_path = os.path.join(account_dir, "new_people.txt")
            try:
                with open(new_file_path, "r") as f:
                    existing_new = [line.strip() for line in f]
            except FileNotFoundError:
                existing_new = []

            with open(new_file_path, "a") as f:
                for person in newly_found_list:
                    if person not in existing_new:
                        f.write(f"{person}\n")

        def record_canceled_people():
            """
            Compares old 'total_people' entries to the current self.all_people_list,
            and appends those who disappeared to 'canceled_people.txt'.
            """
            canceled_file_path = os.path.join(account_dir, "canceled_people.txt")
            total_people_path = os.path.join(account_dir, "total_people")

            # Read old people
            try:
                with open(total_people_path, "r") as f:
                    old_people = [line.strip() for line in f]
            except FileNotFoundError:
                print("No 'total_people' file found, cannot determine canceled people.")
                return

            old_set = set(old_people)
            current_set = set(self.all_people_list)

            # canceled are those who used to be present, but are no longer
            canceled_set = old_set - current_set
            if not canceled_set:
                return  # no one canceled

            # read existing canceled
            try:
                with open(canceled_file_path, "r") as f:
                    already_canceled = [line.strip() for line in f]
            except FileNotFoundError:
                already_canceled = []

            # record newly canceled
            with open(canceled_file_path, "a") as f:
                for person in canceled_set:
                    if person not in already_canceled:
                        f.write(f"{person}\n")

        # Run the steps
        process_existing_people()
        record_new_people()
        record_canceled_people()