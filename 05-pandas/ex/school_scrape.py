import requests
from bs4 import BeautifulSoup

import wget
import xml.etree.ElementTree as et

import pprint

import pandas as pd

from time import sleep

district_html = "http://illinoisreportcard.com/District.aspx?source=SchoolsInDistrict&Districtid=15016299025"
address_html  = "https://iircapps.niu.edu/Apps_2_0/en/School/{}/Profile?helperUrl=//illinoisreportcard.com/helper.html"
perform_html  = "http://iircapps.niu.edu/Internal/MergeResourceView?resourceType=Profile&viewType=Excel&resources=https%3A%2F%2Fiircapi.niu.edu%2FReportCardService%2F(En)%2FDomain(School)%2FId({})%2F(Profile)%2F(2015)%2FTable%2F(Xml)&resources=https%3A%2F%2Fiircapi.niu.edu%2FReportCardService%2F(En)%2FDomain(District)%2FId(15016299025)%2F(Profile)%2F(2015)%2FTable%2F(Xml)&resources=https%3A%2F%2Fiircapi.niu.edu%2FReportCardService%2F(En)%2FDomain(State)%2FId(IL)%2F(Profile)%2F(2015)%2FTable%2F(Xml)&querystrings.title=Fast+Facts"


## GET THE BASE INFORMATION -- ID AND GRADES
r = requests.get(district_html)
soup = BeautifulSoup(r.content, "html.parser")
rows = soup.find("div", "table-striped").find_all("div", "row")

schools = []
for x in rows[1:]:
    
    divs = list(x.find_all("div"))    
    links = divs[0].find_all('a')[0]
    
    school = {}
    school["ISBE_ID"] = links.get('href').split("=")[1]
    school["Name"]    = divs[0].string

    if len(divs) == 3:
        school["Grades"] = divs[1].string
        school["Ready for Next"] = divs[2].string
           
    schools.append(school)
    

## GET THE ADDRESSES FOR GEOCODING
for sid, school in enumerate(schools):

    sleep(0.5)
    school_id = school["ISBE_ID"]
    
    requ_addr = requests.get(address_html.format(school_id))
    soup_addr = BeautifulSoup(requ_addr.content, "html.parser")

    print(school["ISBE_ID"], school["Name"], requ_addr.status_code)
    
    street, city, state, zipc, zip4 = None, None, None, None, None
    
    if soup_addr.find("span", "street").contents:
        street = soup_addr.find("span", "street").contents[0]
    
    zip_contents = soup_addr.find("span", "city-state-zipcode").contents
    if zip_contents and len(zip_contents[0].split()) == 4:
        city, state, zipc, zip4 = zip_contents[0].split()
        
        schools[sid]["Address"] = street
        schools[sid]["City"]    = city
        schools[sid]["Zip"]     = zipc
        schools[sid]["State"]   = state
         

## GET THE FAST FACTS AND PARSE IT
for sid, school in enumerate(schools):
    
    sleep(2)
    print(school["ISBE_ID"], school["Name"])

    school_id = school["ISBE_ID"]
    
    wget.download(url = perform_html.format(school_id), 
                  out = "fast_facts_{}.xls".format(school_id))

    line = next(open("fast_facts_{}.xls".format(school_id)))
    root = et.fromstring(line)
    for x in root[1][0][16]: print(x[0].text)

    titles = [c[0].text for c in root[1][0][24]]
    values = [c[0].text for c in root[1][0][25]]
    
    for t, v in zip(titles, values):
        schools[sid][t] = v
    
ch = pd.DataFrame(schools)
df_sch.set_index("ISBE_ID", inplace = True)
df_sch.to_csv("../data/chicago_schools.csv")

