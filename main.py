import requests
import lxml
from bs4 import BeautifulSoup
import datetime as dt
import smtplib

url = "https://www.amazon.com/Backpack-Business-Charging-Resistant-C" \
      "omputer/dp/B06XZTZ7GB/ref=sr_1_4?qid=1691664998&s=computers-intl-ship&sr=1-4"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,ar;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")


product_cost = soup.find(name="span", class_="a-price-whole")
product_fraction = soup.find(name="span", class_="a-price-fraction")

actual_cost = float(product_cost.getText() + product_fraction.get_text())

now = dt.datetime.now()

if actual_cost <= 100.0:
    connection = smtplib.SMTP("")
    connection.starttls()
    connection.login()
    connection.sendmail(msg=f"product is {actual_cost}$")




