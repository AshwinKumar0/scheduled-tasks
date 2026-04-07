import datetime as dt
import pandas as pd
import random
import smtplib
import os

now = dt.datetime.now()
today = (now.month, now.day)

df = pd.read_csv("birthdays.csv")

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in df.iterrows()}

if today in birthdays_dict:
    value = birthdays_dict[today]
    #parts = value.split(",")
    #name = parts[0]
    #email = parts[1]
    random_number = random.randint(1,3)
    with open(f"letter_templates/letter_{random_number}.txt", "r") as f:
        letter = f.read()
        edited_letter = letter.replace("[NAME]", value["name"])
        print(edited_letter)
else:
    print("No birthdays today.")


MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=email,
        msg=f"Subject: Happy Birthday\n\n{edited_letter}"
    )


