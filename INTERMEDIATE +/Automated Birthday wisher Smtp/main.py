from datetime import datetime
from pandas import read_csv
from random import randint
from smtplib import SMTP

MY_EMAIL = "jay123gaur@gmail.com"
PASSWORD = "1234@Bhav"

today = (datetime.now().month, datetime.now().day)
data = read_csv('birthdays.csv')
birthdays = {(data_row.month, data_row.day):data_row for (index, data_row) in data.iterrows()}
if today in birthdays:
    birthday_person = birthdays[today]
    file_path = f"letter_templates/letter_{randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person['name'])

    with SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person.email,
            msg = f"Subject:HAPPY BIRTHDAY\n\n{contents}"
        )
