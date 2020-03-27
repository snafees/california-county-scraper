# -*- coding: utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
import time

alameda = "https://app.powerbigov.us/view?r=eyJrIjoiODI1YmRlMjUtODUwOC00ZDE0LWExMjMtMjA2ZDI2MTRlMGE4IiwidCI6IjBhYzMyMDJmLWMzZTktNGY1Ni04MzBkLTAxN2QwOWQxNmIzZiJ9" 
driver = webdriver.Chrome('./chromedriver')
driver.get(alameda)

time.sleep(10)
html = driver.page_source
soup = BeautifulSoup(html)

print(soup.prettify())

# Select Figures
positiveCases = soup.find_all("text", {"class": "value"})[0].title.contents[0]

deathsRaw = soup.find("table", {"class": "contacts_table"}).div.select('em')[1].contents[0]

# Remove *
positiveCasesClean = positiveCasesRaw.replace("*", "")
deathsClean = deathsRaw.replace("*", "")