# -*- coding: utf-8 -*-

# Imports. Make sure webdriver is executable by running 'chmod +x ./chromedriver' in directory
from selenium import webdriver
from bs4 import BeautifulSoup
from append import append

sonoma = "https://socoemergency.org/"
driver = webdriver.Chrome('./chromedriver')
driver.get(sonoma)
html = driver.page_source
soup = BeautifulSoup(html, features="html.parser")

# Select Figures
content = soup.findAll("table", {"class": "cvTable"})[0].findAll("td")

totalCases = content[0].contents[0]
activeCases = content[1].contents[0]
recoveredCases = content[2].contents[0]
deaths = content[3].contents[0]
tests = content[4].contents[0]

# Append to JSON File
append('sonoma', totalCases, activeCases, deaths, recoveredCases, tests) 
