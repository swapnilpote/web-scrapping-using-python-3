# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 00:01:26 2016

@author: swapnilpote
"""

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

for letter in ascii_lowercase:
    
    if letter != 'x':
        soup = make_soup("http://www.basketball-reference.com/players/" + letter)
        
        for record in soup.findAll('tr'):
            playerdata = ""
            
            for data in record.findAll('th'):
                playerdata = playerdata + "," + data.text
                
            for data in record.findAll('td'):
                playerdata = playerdata + "," + data.text
            
            if len(playerdata) != 0:
                playerdatasaved = playerdatasaved + "\n" + playerdata[1:]  


file = open(os.path.expanduser("Basketball.csv"),"wb")
file.write(bytes(playerdatasaved, encoding="ascii",errors='ignore'))