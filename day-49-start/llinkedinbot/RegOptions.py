import time
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Registrations:
    def __init__(self, linkedinURL, userEmail, userPassword, userPhone, jobTitle=None):
        """
        This constructor sets up the required parameters and creates a WebDriver instance for browser automation.

        Args:
            linkedinURL (str): The URL of the LinkedIn job search page.
            userEmail (str): The user’s email or username for login.
            userPassword (str): The user’s password for login.
            userPhone (str): The user’s phone number (used on forms).
            jobTitle (str): A specific job title to search for (optional).
        """
        self.userEmail = userEmail
        self.userPassword = userPassword
        self.userPhone = userPhone
        self.linkedinURL = linkedinURL
        self.jobTitle = jobTitle

        self.browser = None
        self.browserWait = None
        self._createBrowser()

        self.nextPage = 2  # Tracks pagination on LinkedIn job listings
        self.appliedCompanies = []  # Stores names of companies to which the user has successfully applied

    def _createBrowser(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=chrome_options)
        self.browserWait = WebDriverWait(self.browser, 5)
        self.browser.get(self.linkedinURL)

    def registration(self):
        """
        Attempts three different login methods to accommodate LinkedIn's different layouts.
        If registration succeeds, asks the user whether to proceed with job applications.
        """
        if self._loginMethod1():
            print("Registration successful via Method 1.")
            userPrompt = input("Do you want to start the application process now? (Yes/No): ").lower()
            if userPrompt == 'yes':
                self._applyToCompanies()
            elif userPrompt == "no":
                print("Exiting...")
            else:
                print("Invalid input.")
        elif self._loginMethod2() or self._loginMethod3():
            print("Registration successful via Method 2 or 3.")
            userPrompt = input("Do you want to start the application process now? (Yes/No): ").lower()
            if userPrompt == 'yes':
                self._searchJob()
            elif userPrompt == "no":
                print("Exiting...")
            else:
                print("Invalid input.")
        else:
            print("All registration methods failed. Please try again later.")

    def _loginMethod1(self):
        try:
            time.sleep(2)
            print("\nAttempting login with Method 1...")

            signInButton = self.browser.find_element(By.XPATH,
                                                     '/html/body/div[4]/div/div/section/div/div/div/div[2]/button')
            signInButton.click()

            time.sleep(1)
            emailField = self.browser.find_element(By.XPATH,
                                                   '/html/body/div[4]/div/div/section/div/div/form/div[1]/div[1]/div/div/input')
            emailField.send_keys(self.userEmail)

            passwordField = self.browser.find_element(By.XPATH,
                                                      '/html/body/div[4]/div/div/section/div/div/form/div[1]/div[2]/div/div/input')
            passwordField.send_keys(self.userPassword, Keys.ENTER)

            input("\nIf there is a CAPTCHA or any manual action needed, please resolve it and press Enter here...")

            print("\nLogin Method 1 completed successfully.")
            return True

        except NoSuchElementException:
            print("\nMethod 1 login failed. Trying Method 2...")
            return False

    def _loginMethod2(self):
        time.sleep(2)
        try:
            print("\nAttempting login with Method 2...")

            loginButton = self.browser.find_element(By.XPATH, '/html/body/div/main/div/form/p/button')
            loginButton.click()

            emailField = self.browser.find_element(By.XPATH,
                                                   '/html/body/div/main/div/div[2]/form/div[1]/div[1]/div/div/input')
            emailField.send_keys(self.userEmail, Keys.ENTER)

            passwordField = self.browser.find_element(By.XPATH,
                                                      '/html/body/div/main/div/div[2]/form/div[1]/div[2]/div/div/input')
            passwordField.send_keys(self.userPassword, Keys.ENTER)

            input("\nIf there is a CAPTCHA or any manual action needed, please resolve it and press Enter here...")

            print("\nLogin Method 2 completed successfully.")
            return True

        except NoSuchElementException:
            print("\nMethod 2 login failed. Trying Method 3...")
            return False

    def _loginMethod3(self):
        time.sleep(2)
        try:
            print("\nAttempting login with Method 3...")

            loginButton = self.browser.find_element(By.XPATH, '/html/body/nav/div/a[2]')
            loginButton.click()

            emailField = self.browser.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[1]/input')
            emailField.send_keys(self.userEmail)

            passwordField = self.browser.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[2]/input')
            passwordField.send_keys(self.userPassword, Keys.ENTER)

            input("\nIf there is a CAPTCHA or any manual action needed, please resolve it and press Enter here...")

            print("\nLogin Method 3 completed successfully.")
            time.sleep(1)
            return True

        except NoSuchElementException:
            print("\nAll login methods exhausted. Unable to register.")
            return False

    def _applyToCompanies(self):
        """
        Scrolls through job listings and retrieves company names.
        Calls the self._applyForSingleJob() method to handle the Easy Apply process if available.
        """
        time.sleep(2)
        visitedJobs = []

        def _scrapeJobsOnPage():
            nonlocal visitedJobs
            jobsOnPage = self.browserWait.until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'ul.rjmNTMLkNvPwnJnFTCybgSFpgYGQ li img'))
            )
            for jobElement in jobsOnPage:
                jobName = jobElement.get_attribute("alt")
                if jobName in visitedJobs:
                    continue
                jobElement.click()
                try:
                    companyNameElement = self.browserWait.until(
                        EC.visibility_of_element_located(
                            (By.CSS_SELECTOR, 'div.job-details-jobs-unified-top-card__company-name a')
                        )
                    )
                    companyName = companyNameElement.text
                    print(f"\nFound job at company: {companyName}")

                    self._applyForSingleJob(companyName)
                    visitedJobs.append(jobName)

                except TimeoutException:
                    print("No company name found. Skipping this listing.")
                    visitedJobs.append(jobName)

        scrollableDiv = self.browser.find_element(By.XPATH,
                                                  '/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div')

        while True:
            _scrapeJobsOnPage()

            previousScrollPosition = self.browser.execute_script("return arguments[0].scrollTop;", scrollableDiv)
            self.browser.execute_script("arguments[0].scrollTop += 700;", scrollableDiv)
            print("Page scrolled successfully...")
            time.sleep(2)

            newScrollPosition = self.browser.execute_script("return arguments[0].scrollTop;", scrollableDiv)

            if newScrollPosition == previousScrollPosition:
                print("Reached the bottom of the current job list.")
                print("Visited job listings:", visitedJobs)
                print("Already applied companies:", self.appliedCompanies)

                # Attempt to go to the next page
                try:
                    print("Trying to navigate to the next page...")
                    nextPageButton = self.browser.find_element(By.CSS_SELECTOR,
                                                               f'div ul li button[aria-label="Page {self.nextPage}"]')
                    nextPageButton.click()
                    self.nextPage += 1
                except NoSuchElementException:
                    print("No more pages available. Exiting browser...")
                    self.browser.quit()
                    break

    def _searchJob(self):
        """
        For registrations done by method2 or method3, we might need to manually
        search a job after login and then apply.
        """
        print(f"\nSearching for job: {self.jobTitle}")
        searchBar = self.browserWait.until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/header/div/div/div/div[1]/input'))
        )
        searchBar.send_keys(self.jobTitle, Keys.ENTER)
        self._filterEasyApplyJobs()

    def _applyForSingleJob(self, companyName=None):
        """
        Clicks on 'Easy Apply' or 'Apply' button to attempt an application.
        Fills out the phone number if needed, and checks if the application is successful or not.
        """

        def checkIfApplied():
            # If application is successful or "Already applied" notice is present, handle & dismiss modal
            try:
                print("Checking if job was instantly applied (Scenario 1)...")
                successMessage = self.browserWait.until(
                    EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div[2]/h3'))
                )
                print("Application submitted successfully!")
                self.appliedCompanies.append(companyName)
                closeModalButton = self.browser.find_element(By.XPATH, '/html/body/div[4]/div/div/button')
                closeModalButton.click()
                return True
            except TimeoutException:
                print("Checking if job was applied (Scenario 2)...")
                try:
                    successMessageAlt = self.browser.find_element(By.CLASS_NAME, 'jpac-modal-header.t-20.t-bold')
                    print("Application submitted (alternative detection).")
                    self.appliedCompanies.append(companyName)
                    return True
                except NoSuchElementException:
                    pass
            except NoSuchElementException:
                # If the "Dismiss" button is present, close it
                dismissButton = self.browser.find_element(By.CSS_SELECTOR, 'div div div button[aria-label="Dismiss"]')
                dismissButton.click()
            return False

        def checkSafetyReminder():
            # Some postings show a "safety" reminder or disclaimers that block easy application
            try:
                print("Looking for safety reminder pop-up...")
                safetyApplyButton = self.browserWait.until(
                    EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div[3]/div/div/button'))
                )
                print("A safety reminder is present. Closing it and skipping this job.")
                closeButton = self.browserWait.until(
                    EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/div/button')))
                closeButton.click()
                return True
            except TimeoutException:
                print("No safety reminder found.")
                return False

        try:
            print(f"Attempting to apply at: {companyName}")
            applyButton = self.browserWait.until(
                EC.element_to_be_clickable((By.XPATH,
                                            '/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div[5]/div/div/div/button'))
            )
            applyButton.click()

            if checkSafetyReminder():
                return

            # Attempt to find phone number input field
            try:
                print("Looking for phone number field (method 1)...")
                phoneField = self.browserWait.until(
                    EC.visibility_of_element_located((By.XPATH,
                                                      '/html/body/div[4]/div/div/div[2]/div/div[2]/form/div/div/div[4]/div/div/div[1]/div/input'))
                )
            except TimeoutException:
                print("Looking for phone number field (method 2)...")
                phoneField = self.browser.find_element(By.CSS_SELECTOR,
                                                       'div.artdeco-text-input--container.ember-view input')
            except NoSuchElementException:
                print("Looking for phone number field (method 3)...")
                phoneField = self.browser.find_element(By.CSS_SELECTOR, 'div.ZxlCPgbyTcaHsoKicgLvkfGYSxPmVqWGqPk input')

            # Fill in phone number if it's empty
            currentPhone = phoneField.get_attribute("value").strip()
            if currentPhone:
                print(f"Phone field already has a value: {currentPhone}")
            else:
                print("Filling phone number...")
                phoneField.send_keys(self.userPhone)

            # Click the first submit button
            try:
                firstSubmit = self.browser.find_element(By.XPATH,
                                                        '/html/body/div[4]/div/div/div[2]/div/div[2]/form/footer/div[2]/button')
                firstSubmit.click()
            except NoSuchElementException:
                print("Trying alternative selector for submit button...")
                try:
                    firstSubmitAlt = self.browser.find_element(By.CSS_SELECTOR,
                                                               'div button[aria-label="Submit application"]')
                    firstSubmitAlt.click()
                except NoSuchElementException:
                    print("Trying second alternative for submit button...")
                    firstSubmitAlt2 = self.browser.find_element(By.CLASS_NAME,
                                                                'artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view')
                    firstSubmitAlt2.click()

            # If applied successfully, do not proceed further
            if checkIfApplied():
                return

            # Check if there are additional steps
            completionPercentage = self.browser.find_element(By.XPATH,
                                                             '/html/body/div[4]/div/div/div[2]/div/div[1]/span').text
            print(f"Application completion at: {completionPercentage}")
            if completionPercentage != "50%":
                print("Additional questions are required. Skipping this job.")
                closeX = self.browserWait.until(
                    EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/div/button')))
                closeX.click()
                discardButton = self.browserWait.until(
                    EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[2]/div/div[3]/button[1]')))
                discardButton.click()
                return

            # If code reaches here, there's a second/third step to finalize the application
            try:
                print("Attempting final submission steps...")
                stepTwoBtn = self.browserWait.until(
                    EC.visibility_of_element_located(
                        (By.CLASS_NAME, 'artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view')
                    )
                )
                stepTwoBtn.click()

                stepThreeBtn = self.browserWait.until(
                    EC.visibility_of_element_located(
                        (By.XPATH, '/html/body/div[4]/div/div/div[2]/div/div[2]/div/footer/div[3]/button[2]')
                    )
                )
                stepThreeBtn.click()

            except TimeoutException:
                print("Trying alternative approach for final submission...")
                stepTwoBtnAlt = self.browser.find_element(By.XPATH,
                                                          '/html/body/div[4]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]')
                stepTwoBtnAlt.click()
                stepThreeBtnAlt = self.browserWait.until(
                    EC.visibility_of_element_located(
                        (By.XPATH, '/html/body/div[4]/div/div/div[2]/div/div[2]/div/footer/div[3]/button[2]')
                    )
                )
                stepThreeBtnAlt.click()

            except NoSuchElementException:
                print("Attempting second alternative approach for final submission...")
                stepTwoBtnAlt2 = self.browser.find_element(By.CSS_SELECTOR,
                                                           'div.display-flex.justify-flex-end.ph5.pv4 button[aria-label]="Review your application"')
                stepTwoBtnAlt2.click()
                stepThreeBtnAlt2 = self.browserWait.until(
                    EC.visibility_of_element_located(
                        (By.XPATH, '/html/body/div[4]/div/div/div[2]/div/div[2]/div/footer/div[3]/button[2]')
                    )
                )
                stepThreeBtnAlt2.click()

            # Check if final submission was successful
            if checkIfApplied():
                return

        except (NoSuchElementException, TimeoutException):
            print("Unable to apply. This job may not support Easy Apply or an error occurred.")
            return

    def _filterEasyApplyJobs(self):
        """
        For login methods 2 or 3, the user might land on the LinkedIn search page
        and then click 'Easy Apply' to see only 'Easy Apply' type jobs.
        """
        time.sleep(1)
        print("\nFiltering to 'Easy Apply' jobs...")
        jobsButton = self.browserWait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[6]/div[3]/div[2]/div/div[1]/div/div/div/section/ul/li[1]/button"))
        )
        jobsButton.click()

        openJobsLink = self.browser.find_element(By.XPATH,
                                                 '/html/body/div[6]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/div[2]/a')
        openJobsLink.click()

        easyApplyFilter = self.browserWait.until(
            EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div[6]/div[3]/div[4]/section/div/section/div/div/div/ul/li[8]/div/button'))
        )
        easyApplyFilter.click()

        self._applyToCompanies()

