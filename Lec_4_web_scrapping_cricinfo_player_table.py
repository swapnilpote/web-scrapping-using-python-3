import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
from string import ascii_lowercase


def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata


playerdatasaved = ""
countries = [2, 25, 1, 6, 5, 7, 3, 8, 4, 9]

for country in countries:
	soup = make_soup("http://www.espncricinfo.com/ci/content/player/index.html?country="+str(country))

	if bool(soup.find('table', {"class":"playersTable"}).text) == True:

		for record in soup.findAll('tr'):
			playerdata = ""

			for data in record.findAll('td'):
				playerdata = playerdata, data.get('href'), data.text
				print(playerdata)
