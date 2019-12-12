#1st step: install requests & bs4 (pip install requests bs4)

import requests
from bs4 import BeautifulSoup #fetches from website
import smtplib #enables to send emails
import time

print('Enter sending email account: ')
mailFrom=input()

print('Enter receiving email account: ')
mailTo=input()

print('Enter password for sending email account: ')
password=input()

URL = 'https://www.notino.de/armani/code-profumo-eau-de-parfum-fur-herren/p-541287/'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}

count = 0
while True:
        count+=1
        print(count)

        def check_price():
                page = requests.get(URL, headers=headers)
                soup = BeautifulSoup(page.content, 'html.parser')
                title = soup.find(id="pdHeader").get_text()
                price = soup.find(id="pd-price").get_text()
                converted_price = float(price[0:2])

                if (converted_price < 77):
                        send_mail()
                        print(title.strip())
                        print('New price: ' + price)
 
        def send_mail():
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.ehlo()

                server.login(mailFrom, password)

                subject = 'Price is lower'
                body = 'Price is lower, check the link: https://www.notino.de/armani/code-profumo-eau-de-parfum-fur-herren/p-541287/'
                msg = f"Subject: {subject}\n\n{body}"

                server.sendmail(
                        mailFrom,
                        mailTo,
                        msg
                )
                print('Email has been sent.')
                server.quit()

        check_price()

        time.sleep(43200) #43200sec = 12 hours




