# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 23:24:58 2016

@author: swapnilpote
"""
import urllib
import urllib.request
from bs4 import BeautifulSoup

theurl = "https://twitter.com/shirleysetia"
thepage = urllib.request.urlopen(theurl)
soup = BeautifulSoup(thepage,"html.parser")

print(soup.title.text)
# print(soup.findAll('a'))

'''
for link in soup.findAll('a'):
    print(link.get('href'))
    print(link.text)
'''

# soup.findAll('a')[0] It will collect only first element
print(soup.find('div', {"class":"ProfileHeaderCard"}).find('p').text)

i = 1
for tweets in soup.findAll('div', {"class":"content"}):
    print(i)    
    print(tweets.find('p').text + "\n")
    i = i + 1