from bs4 import BeautifulSoup

from selenium import webdriver

driver = webdriver.Firefox()

driver.get('https://twitter.com/swapnilp0te')

html = driver.page_source

soup = BeautifulSoup(html)

for tag in soup.findAll('div', {"class":"content"}):
	print(tag.text)