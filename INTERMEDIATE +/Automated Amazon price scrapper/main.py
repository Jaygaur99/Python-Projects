import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

BUDGET = 1500
USERNAME = ""  # YOUR USERNAME HERE
PASSWORD = ""  # YOUR PASSWORD HERE

URL = "https://www.amazon.in/JBL-Bluetooth-Headphones-Multi-Point-Connection/dp/B08FB2LNSZ/ref=sr_1_1_" \
      "sspa?dchild=1&keywords=jbl+earphones&qid=1619094054&smid=A14CZOWI0VEHLG&sr=8-1-spons&psc=1&spLa=ZW5" \
      "jcnlwdGVkUXVhbGlmaWVyPUEzQzk2SUwwMTVQNzNQJmVuY3J5cHRlZElkPUEwMzE4ODc1MVFRVlVHQzhON1IySSZlbmNyeXB0ZWRB" \
      "ZElkPUEwNzM0NjE0MlhTMk02WEUzWEVCQyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.content, 'lxml')
price = soup.find('span', id="priceblock_dealprice").getText().split()[1]
new_price = price.split(',')
price = float(''.join(new_price))

if price < BUDGET:
    title = soup.find(id="productTitle").get_text().strip()
    print(title)
    msg = f"{title} is now {price}"

    connection = smtplib.SMTP('smtp.gmail.com', port=587)
    connection.starttls()
    connection.login(user=USERNAME, password=PASSWORD)
    connection.sendmail(
        from_addr=USERNAME,
        to_addrs=USERNAME,
        msg=f"Subject:Amazon Price Alert!\n\n{msg}\n{URL}"
    )
