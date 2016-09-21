import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
from string import ascii_lowercase

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

soup = make_soup("https://www.tripadvisor.in/Hotel_Review-g60763-d292142-Reviews-Dumont_NYC_an_Affinia_hotel-New_York_City_New_York.html#REVIEWS")

link = soup.find(attrs={"class":"nav next rndBtn ui_button primary taLnk"})
print(link.get('href'))
