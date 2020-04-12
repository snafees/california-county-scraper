# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import simplejson as json
from datetime import date

### SCRAPE ###
url = "https://www.sfdph.org/dph/alerts/coronavirus.asp"
page = requests.get(url)
contents = page.content
soup = BeautifulSoup(contents, 'html.parser')

positiveCasesRaw = soup.find_all("div", {"id": "helpful-links"})[1].p.contents[0]
deathsRaw = soup.find_all("div", {"id": "helpful-links"})[1].find_all('p')[1].contents[0]

#String Replace
positiveCasesClean = positiveCasesRaw.replace("Total Positive Cases: ", "")
deaths = deathsRaw.replace("Deaths: ", "")


### APPEND TO JSON FILE ###
append('san_francisco', 'N/A', positiveCasesClean, deaths, 'N/A', 'N/A')
