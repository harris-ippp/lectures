import requests
from bs4 import BeautifulSoup

sch_ad =  "https://iircapps.niu.edu/Apps_2_0/"
sch_ad += "/en/School/150162990250849/Profile?"
sch_ad += "helperUrl=//illinoisreportcard.com/helper.html"

resp = requests.get(sch_ad)
soup = BeautifulSoup(resp.content, "html.parser")

street = soup.find("span", "street").contents[0]

