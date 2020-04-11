# -*- coding: utf-8 -*-

# Imports. Make sure webdriver is executableby running 'chmod +x ./chromedriver' in directory

from selenium import webdriver
from bs4 import BeautifulSoup
from append import append
import time

sonoma = "https://ac-hcsa.maps.arcgis.com/apps/opsdashboard/index.html#/948c67558cff414dbbee1a78fcbab1c9"
driver = webdriver.Chrome('./chromedriver')
driver.get(sonoma)
time.sleep(10)

html = driver.page_source
soup = BeautifulSoup(html, features="html.parser")

# Select Figures
positiveCasesRaw = soup.find("full-container").findAll("div")[4]
print(positiveCasesRaw)
