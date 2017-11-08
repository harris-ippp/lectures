#import urllib3
import bs4
#import urllib.parse
import requests
import re
#from argparse import ArgumentParser

def get_courses():
  
	main_url = 'http://collegecatalog.uchicago.edu/thecollege/programsofstudy/'

	course_url = 'http://collegecatalog.uchicago.edu/thecollege/{}/'

	request = requests.get(url= main_url)
	html = request.content

	#this is a BeautifulSoup Object that parses the page into its html elements
	#so that we can search if using other BeautifulSoup methods
	soup = bs4.BeautifulSoup(html,'html.parser')

	programs = soup.find('ul', class_ = "leveltwo")

	course_areas = [item.text 
	for item in programs.find_all('a') 
		if len(item["href"]) !=0 ]

	course_urls = [item["href"] for item in programs.find_all('a') if item["href"]]


	return course_areas

def get_articles_pro(complement):
    '''
    '''
    propublica = 'https://www.propublica.org/archive/{}'
    #archive_url = propublica +complement+'/'
    archive_url = propublica.format(complement)
    articles = {}
    request = requests.get(url= archive_url)
    html = request.content

	#this is a BeautifulSoup Object that parses the page into its html elements
	#so that we can search if using other BeautifulSoup methods
    soup = bs4.BeautifulSoup(html,'html.parser')

    tag_list = soup.find_all('a', title = 'View this')

    rv= {}

    if tag_list:
        for index,tag in enumerate(tag_list):
            
            rv[index] = {'article':tag.text}
            rv[index]['pub_date'] = complement
            
        return rv

date = '2017/10'

print(get_articles_pro(date))