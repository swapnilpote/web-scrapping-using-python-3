from selenium import webdriver
import time
import csv

chrome_path = '/Users/swapnilpote/Downloads/chromedriver'

driver = webdriver.Chrome(chrome_path)

driver.get('https://twitter.com/realDonaldTrump')


# while True:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

SCROLL_PAUSE_TIME = 2
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
print("Last Height 1", last_height) # Testing purpose comment

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    print("Last Height 2", last_height) # Testing purpose comment

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")

    print("New Height", new_height) # Testing purpose comment


    if new_height == last_height:
        break

    last_height = new_height

    tweets = driver.find_elements_by_class_name("tweet-text")

    for tweet in tweets:
        tweet = tweet.text

        saveFile = open('tweets.csv', 'a')
        saveFile.write(tweet)
        saveFile.write('\n')
        saveFile.close()
