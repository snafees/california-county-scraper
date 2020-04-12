# Sonoma County
from bs4 import BeautifulSoup
from scraper_init import scrape
from append import append

# Init Scraper and Return Soup
soup = scrape('https://socoemergency.org/', 5)

# Select Figures
content = soup.findAll("table", {"class": "cvTable"})[0].findAll("td")
print(content)

totalCases = content[0].contents[0]
activeCases = content[1].contents[0]
recoveredCases = content[2].contents[0]
deaths = content[3].contents[0]
tests = content[4].contents[0]

# Append to JSON File
append('sonoma', totalCases, activeCases, deaths, recoveredCases, tests)
