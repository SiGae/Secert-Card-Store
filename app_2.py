from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep


def easter_egg():
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    driver.get('http://its.go.kr/traffic/condition.do')
    sleep(5)

    h = driver.page_source

    root = BeautifulSoup(h, 'html.parser')
    a = root.find_all('ul', {'id': 'congestedAreaList'})

    z = ""
    for i in a:
        z += i.get_text()
    return z
