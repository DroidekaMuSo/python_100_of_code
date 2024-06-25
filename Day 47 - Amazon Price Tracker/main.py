import requests
from bs4 import BeautifulSoup
import smtplib
import os
import dotenv
import lxml

dotenv.load_dotenv()

product_url = ("https://www.amazon.com.mx/Nintendo-Switch-Splatoon-Special-Internacional/dp/B0BDSJ8DR7/ref=sr_1_1?crid"
               "=1XIOUQH0VLM1J&dib=eyJ2IjoiMSJ9.BNc--eFRWlQBGu43QsTJe37pJr87nKw0OGS44lpiiYeAd16cZRcBmmN2"
               "-eimG9uuAb5l5MuQdz3uZU1KnzIAqXF-VJFHTtbem0hvyo2BiBMwyYEC9tJHiyqAqiD9ys4kML6hxuNRmD_devcxj6b4IqY3i-2CI"
               "-09gEx_psT2O2fuf1Gn1XRYsGWmJf7_JpiObT_7aU--4kkRb5ky3"
               "-VktISKnRxSB4pIvOk3EqXGP8pzRy8xFuIMnHqMZ2ZzH4VAwsPW3pVNyXoBewab3cCQ7H_ilRJA_7EuuZSFXxe67Gs"
               ".8YOww4H8GIPiBlwcjBjU6Zvxcr1fpIt0qnUwCWpteGo&dib_tag=se&keywords=nintendo%2Bswitch%2Boled%2Bsplatoon"
               "&qid=1719350379&sprefix=nintendo%2Bswitch%2Boled%2Bsplatoo%2Caps%2C133&sr=8-1&ufe=app_do%3Aamzn1.fos"
               ".628a2120-cf12-4882-b7cf-30e681beb181&th=1")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(url=product_url, headers=headers)
product_data = response.text

soup = BeautifulSoup(product_data, "lxml")


def send_email(message):
    connection = smtplib.SMTP(os.environ.get("EMAIL_PROVIDER_SMTP_ADDRESS"))
    connection.starttls()
    connection.login(user=os.environ.get("GOOGLE_EMAIL"), password=os.environ.get("GOOGLE_PASSWORD"))

    connection.sendmail(
        from_addr=f"{os.environ.get("GOOGLE_EMAIL")}",
        to_addrs=f"{os.environ.get("GOOGLE_EMAIL")}",
        msg=message.encode("utf-8"),

    )


whole_number = soup.find(name="span", class_="a-offscreen").getText()
cleaned_price = float(whole_number.split("$")[1].replace(",", ""))
product_title = soup.find(name="span", id="productTitle").getText().strip()
message = f"Subject:Amazon Price Alert!!\n\n{product_title} is now ${cleaned_price}\n\nGo for it {product_url}"

if cleaned_price < 6000:
    send_email(message)
