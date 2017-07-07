import urllib
import urllib.request
from bs4 import BeautifulSoup

theurl = "https://twitter.com/AndrewYNg"
thepage = urllib.request.urlopen(theurl)
# print(thepage)



soup = BeautifulSoup(thepage, "html.parser")
# print(soup)

# print(soup.title.text)
#
# print(soup.findAll('a'))
#
#
# for link in soup.findAll('a'):
#     print(link.get('href'))
    # print(link.text)

# soup.findAll('a')[0] It will collect only first element
print(soup.find('div', {"class":"ProfileHeaderCard"}).find('p').text)

'''
for tweets in soup.findAll('div', {"class":"content"}):
    print(tweets.find('p').text + "\n")
'''
