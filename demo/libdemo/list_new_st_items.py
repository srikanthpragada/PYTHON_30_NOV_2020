import requests
from bs4 import BeautifulSoup

ROOT = "http://www.srikanthtechnologies.com/rss.xml"
resp = requests.get(ROOT)
bs = BeautifulSoup(resp.text, "lxml-xml")
items = bs.find_all("item")[:10]

for item in items:
    title = item.find("title").text
    link = item.find("link").text
    print(title.strip())
    print(link.strip())
    print("-" * 80)
