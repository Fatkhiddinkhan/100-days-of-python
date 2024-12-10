##################### Extra Hard Starting Project ######################
import datetime as dt
import smtplib
import pandas
import random

my_email = "put here you email"
my_password = "put here your toke"

## time configurations
now = dt.datetime.now()
day = now.day
month = now.month

data = pandas.read_csv("birthdays.csv")
people_info = data.to_dict(orient="records")
#----------------------#
def load_templates(directory="letter_templates"):
    templates = []
    for i in range(1,4):
        with open(f"{directory}/letter_{i}.txt") as file:
            templates.append(file.read())
    return templates

for item in people_info:
    if month == item["month"] and day == item["day"]:
        print(item)
        birthday_letter = random.choice(load_templates())
        birthday_letter = birthday_letter.replace("[NAME]", item["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=item["email"],
                                msg=f"Subject:Birthday Wish\n\n{birthday_letter}")




