import requests
from bs4 import BeautifulSoup
class AmazonData:
    def __init__(self, url, email, price):
        self.url = url
        self.email = email
        self.user_des_price = price

        self.current_price = None
        self.product_name = None
        self.product_des_price = 0

        self.search_product()
    def search_product(self):
        headers = {'Accept-Language': "en-US,en;q=0.9,ko;q=0.8",
                   'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}

        response = requests.get(url=self.url, headers=headers)
        if response.status_code == 200:
            print(response.status_code)
            self.soup = BeautifulSoup(response.content, "html.parser")
            product_text = self.soup.find(id="productTitle").get_text()
            product_text_clean = " ".join(product_text.split())
            self.product_name = product_text_clean
            print(f"Product: {self.product_name}, found.")
        else:
            print("Invalid url")

    def search_price(self):
        price = float(self.soup.find(class_="aok-offscreen").text.split("$")[1])
        self.current_price = price
        if price > 0:
            print(f"Current price for product: {price}")
            if self.current_price < self.user_des_price:
                print("Price below desired price.!")
                self.product_des_price = self.user_des_price
        else:
            print("Product out of sail")
