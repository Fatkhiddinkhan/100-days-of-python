import random
import smtplib
import datetime as dt


my_email = "Here put your email address"
my_password = "Here put your password"


now = dt.datetime.now()
week = now.weekday()
if week == 1:
    with open("quotes.txt") as quote_file:
        all_quote = quote_file.readlines()
        quote = random.choice(all_quote)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject: Monday motivation\n\n{quote}")