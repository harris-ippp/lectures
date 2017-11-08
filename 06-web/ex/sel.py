from selenium import webdriver

addr = "http://illinoisreportcard.com/District.aspx?"
addr += "source=schoolsindistrict&Districtid=15016299025"

driver = webdriver.PhantomJS()
driver.get(addr)
driver.page_source # like requests.get(...).text
