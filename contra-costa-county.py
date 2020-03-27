# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

url = "https://www.coronavirus.cchealth.org/" 
page = requests.get(url)
contents = page.content
soup = BeautifulSoup(contents, 'html.parser')

positiveCases = soup.body.find(id="comp-k7p0eq5v").h1.span.span.contents[0]
deaths = soup.body.find(id="comp-k7p0g5md1").h1.span.span.contents[0]