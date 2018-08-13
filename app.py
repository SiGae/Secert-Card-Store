from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait

rank = [] 
driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(3)
driver.get('http://dolivago.com/')
sleep(20)

h = driver.page_source

root = BeautifulSoup(h,'html.parser')
a = root.find_all('tr', class_='MuiTableRow-root-30')

print(a[1].get_text())
for i in range(10):
    rank.append(a[i].get_text())
print(rank)
