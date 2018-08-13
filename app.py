from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep


def craw():
    rank = []
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    driver.get('http://dolivago.com/')
    sleep(5)

    h = driver.page_source

    root = BeautifulSoup(h, 'html.parser')
    a = root.find_all('tr', class_='MuiTableRow-root-30')

    for i in range(10):
        rank.append(a[i].get_text())
    print(rank)
    return rank


