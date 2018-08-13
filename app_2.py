from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait

delay = []
driver = webdriver.Firefox()
driver.implicitly_wait(3)
driver.get('http://its.go.kr/traffic/condition.do')
sleep(5)

h = driver.page_source

root = BeautifulSoup(h,'html.parser')
a = root.find_all('ul', {'id':'congestedAreaList'})

for i in range(len(a)):
    delay.append(a[i].get_text())
print(delay)
