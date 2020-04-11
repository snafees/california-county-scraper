# -*- coding: utf-8 -*-

# Imports. Make sure webdriver is executable by running 'chmod +x ./chromedriver' in directory
from selenium import webdriver
from bs4 import BeautifulSoup

berkeley = "https://www.cityofberkeley.info/coronavirus/"
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)
driver.get(berkeley)
html = driver.page_source
soup = BeautifulSoup(html, features="html.parser")

positiveCases = soup.find_all('strong')[0].contents[0]
print(positiveCases)
