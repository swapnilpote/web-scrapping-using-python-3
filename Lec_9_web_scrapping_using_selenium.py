from selenium import webdriver

chrome_path = '/Users/swapnilpote/Downloads/chromedriver'

driver = webdriver.Chrome(chrome_path)

driver.get('http://www.zomato.com')

driver.find_element_by_xpath("""/html/body/section[1]/div/div/div/div[3]/div/a""").click()

restaurants = driver.find_elements_by_class_name("res_title")


for res in restaurants:
    print(res.text)
