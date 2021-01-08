import requests
from bs4 import BeautifulSoup
import datetime

ROOT = "http://www.srikanthtechnologies.com"
resp = requests.get(ROOT)
bs = BeautifulSoup(resp.text, "html.parser")
table = bs.find(id='ctl00_ContentPlaceHolder1_GridView2')
for row in table.find_all("tr")[1:]:
    cols = row.find_all("td")
    title = cols[0].text
    timings = cols[1].text
    stdate = cols[2].text
    # Convert stdate(dd-mon) to date
    sysdate = datetime.datetime.now()
    year = sysdate.year
    startdate= datetime.datetime.strptime(stdate + "-" + str(year), '%d-%b-%Y')
    days = (startdate - sysdate).days
    print(f"{title:50} {timings:15} {days} days to go")
