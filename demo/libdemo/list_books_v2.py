import requests
from bs4 import BeautifulSoup

f = open("books2.xml", "rt")
bs = BeautifulSoup(f.read(), "lxml-xml")
books = bs.find_all("book")
for book in books:
    title = book['title'] # Attribute title
    price = book['price'] # Attribute price
    print(f"{title:30} {price:5}")

f.close()
