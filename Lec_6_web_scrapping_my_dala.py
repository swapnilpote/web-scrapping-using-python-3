import urllib
import urllib.request
from bs4 import BeautifulSoup

def make_soup(url):
	page = urllib.request.openurl(url)
	soupdata = BeautifulSoup(page, "html.parser")
	return soupdata

theurl = "http://www.mydala.com/"
thepage = urllib.request.urlopen(theurl)
soup = BeautifulSoup(thepage, "html.parser")

navlinks = [] # nav bar links of categories
for navlink in soup.findAll('div', {"class":"fltLeft nav-wrapper"}):
	for i in navlink.findAll('a'):
		navlinks.append(i.get('href'))

print(navlinks) # nav bar links of categories






pagelink = []
for pagelink in navlinks:
	for page_number in pagelink.findAll(pagination fltRight suffix-8)

	'''
	page = urllib.request.urlopen(link)
	newsoup = BeautifulSoup(page, "html.parser")

	for single_item_link in newsoup.findAll('div', {"class":"search-merchant-nugget clearfix"}):
		print(single_item_link.find('span',{"class":"font-bold darkgrey-txt"}))
	'''
