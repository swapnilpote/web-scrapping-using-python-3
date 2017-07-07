import urllib
import urllib.request
from bs4 import BeautifulSoup

# This function going to work as web scraper entry point for every link n return complete page in html format
def make_soup(url):
	page = urllib.request.urlopen(url)
	soupdata = BeautifulSoup(page, 'html.parser')
	return soupdata
