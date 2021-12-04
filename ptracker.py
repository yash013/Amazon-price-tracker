import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/New-Apple-iPhone-Pro-256GB/dp/B08L5T31M6/ref=sr_1_3?crid=2KSUM6V5N1Q3L&dchild=1&keywords=iphone+12+pro+max+%2B%2B%2B%2B%2B&qid=1629795530&sprefix=ip%2Caps%2C713&sr=8-3'


headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
def check_price():

    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())

    title = soup.find(id = 'productTitle').get_text()
    price = soup.find(id = 'priceblock_ourprice').get_text()
    converted_price = float(price[1:9].replace(",",""))

    if converted_price < 129999:
        sendmail()

    print(title.strip())
    print(converted_price)

    if converted_price < 129999:
        sendmail()

def sendmail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('youremail@gmail.com', 'gupicptrfsaabqpf')

    subject = "Hey! The price fell down"
    body = "Check the amazone link https://www.amazon.in/New-Apple-iPhone-Pro-256GB/dp/B08L5T31M6/ref=sr_1_3?crid=2KSUM6V5N1Q3L&dchild=1&keywords=iphone+12+pro+max+%2B%2B%2B%2B%2B&qid=1629795530&sprefix=ip%2Caps%2C713&sr=8-3"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('reciversemailid@gmail.com', 'emailidthatsendsyouemail@gmail.com', msg)

    print("HEY! EMAIL HAS BEEN SENT")

    server.quit()

# check_price()

# while(True):
#     check_price()
#     time.sleep(60*60)