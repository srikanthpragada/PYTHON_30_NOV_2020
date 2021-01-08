import requests
from bs4 import BeautifulSoup

f = open("books.xml","rt")
bs = BeautifulSoup(f.read(), "lxml-xml")
books = bs.find_all("book")
for book in books:
    title = book.find("title").text
    price = book.find("price").text
    print(f"{title:30} {price:5}")

f.close()
