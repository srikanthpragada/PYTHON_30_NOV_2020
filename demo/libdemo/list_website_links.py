import requests
from bs4 import BeautifulSoup

website = input("Enter website :")
try:
    resp = requests.get(website)
    if resp.status_code != 200:
        print("Sorry! Could not connect to website!")
        exit(1)
except:
    print('Sorry! Could not access website!')
    exit(2)

bs = BeautifulSoup(resp.text, "html.parser")
links = bs.find_all("a")
print("Number of links : ", len(links))

stlinks = []
for link in links:
    # if href attr is not found
    if not 'href' in link.attrs:
        continue

    href = link['href']
    if href == '#':
        continue

    if not href.startswith("http"):
        href = website + (href if href.startswith("/") else '/' + href)
        if href not in stlinks:
            stlinks.append(href)

for link in stlinks:
    print(link)
