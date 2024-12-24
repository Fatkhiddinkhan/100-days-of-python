
from smtplib import SMTP
from dotenv import load_dotenv
from amazon_data import AmazonData
import os
load_dotenv()

user_prompt = input("Enter product URL: ").lower()
user_email = input("Enter your Email: ").lower()
user_desired_price = float(input("Enter your Desired Price: $"))
###------URLS------###
# amazon_test_url = "https://appbrewery.github.io/instant_pot/"
# amazon_url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
my_email = os.environ.get("MY_EMAIL")
app_password = os.environ.get("APP_PASSWORD")
smtp_address = os.environ.get("SMTP_ADDRESS")
if user_desired_price > 1 and len(user_prompt) > 1 and len(user_email) > 1:
    amazon = AmazonData(user_prompt, my_email, user_desired_price)
    amazon.search_price()

###------MESSAGE-----###
    Subject = "Amazon price alert"
    Body = f"Price for {amazon.product_name} is bellow decired price"
    msg = f"Subject: {Subject}\n\n{Body}"
    if amazon.product_des_price > 0:
        with SMTP(smtp_address) as server:
            server.starttls()
            server.login(user=my_email, password=app_password)
            server.sendmail(from_addr=my_email, to_addrs=user_email, msg=msg.encode("utf-8"))
else:
    print("Invalid input")