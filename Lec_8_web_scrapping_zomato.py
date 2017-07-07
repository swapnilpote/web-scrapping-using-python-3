from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Read It Online')
type(linkElem)
linkElem.click() # follows the "Read It Online" link




'''
import urllib
import urllib.request
from bs4 import BeautifulSoup

def make_soup(url):
	page = urllib.request.urlopen(url)
	soup = BeautifulSoup(page, 'html.parser')
	return soup


soup_data = make_soup('https://www.zomato.com/indore/mangosteen-cafe-new-palasia/reviews')

for comment_text in soup_data.findAll('div', {'itemprop':'review'}):
	print(comment_text.text)
'''
