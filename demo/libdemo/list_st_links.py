import requests
from bs4 import BeautifulSoup

ROOT = "http://www.srikanthtechnologies.com"
resp = requests.get(ROOT)
bs = BeautifulSoup(resp.text, "html.parser")
links = bs.find_all("a")
print("Number of links : ", len(links))

stlinks = []
for link in links:
    href = link['href']
    if href == '#':
        continue

    if not href.startswith("http"):
        href = ROOT + "/" + href
        if href not in stlinks:
            stlinks.append(href)

for link in stlinks:
    print(link)
