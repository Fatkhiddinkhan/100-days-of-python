from RegOptions import Registrations

LINK = "Enter linkedin link"
USERNAME = "Enter your email"
PASSWORD = "Enter your password"
MOBILE_NUM = "Your mobile number"
JOB = "python developer"

driver = Registrations(linkedinURL=LINK, userEmail=USERNAME, userPassword=PASSWORD, userPhone=MOBILE_NUM, jobTitle=JOB)

driver.registration()