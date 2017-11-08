import requests
from bs4 import BeautifulSoup

sch_ad =  "http://iircapps.niu.edu/Apps_3_0/"
sch_ad += "/en/School/150162990250849/Profile"

resp = requests.get(sch_ad)
soup = BeautifulSoup(resp.content, "html.parser")

street = soup.find("span", "street").contents[0]
