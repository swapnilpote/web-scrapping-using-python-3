import urllib
import urllib.request
from bs4 import BeautifulSoup
import csv

theurl = "http://www.amazon.in/gp/bestsellers/computers/1375424031/ref=zg_bs_1375424031_pg_1?ie=UTF8&pg=1"

thepage = urllib.request.urlopen(theurl)
soup = BeautifulSoup(thepage,"html.parser")

page_link = []
for link in soup.findAll('li', {"class":"zg_page"}):
	page_link.append(link.find('a').get('href'))

print(page_link)


for newurl in page_link:
	print(newurl)
	thepage = urllib.request.urlopen(newurl)
	soup = BeautifulSoup(thepage,"html.parser")

	for laptopItem in soup.findAll('div', {"class":"zg_itemWrapper"}):

		try:
			name = laptopItem.find('div', {"class":"p13n-sc-truncated-hyphen"}).text.strip()
			price = laptopItem.find('span', {"class":"a-size-base"})
			price = price.text.encode('ascii', 'ignore').decode('ascii')

			saveFile = open('amazon.csv', 'a')
			saveFile.write(name)
			saveFile.write(price)
			print(name)
			print(price)
			saveFile.write('\n')
			saveFile.close()
		except AttributeError:
			pass
