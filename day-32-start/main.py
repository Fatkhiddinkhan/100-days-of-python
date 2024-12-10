"""first time sending email through python code """

import smtplib
my_email = "put here you email"
my_password = "put here your toke"

with smtplib.SMTP("smtp.gmail.com.") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="put here receiver",
                        msg="Subject:Hello\n\nIt is my first email with Python")
