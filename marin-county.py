# Marin County
from bs4 import BeautifulSoup
from scraper_init import scrape
from append import append

# Init Scraper and Return Soup
soup = scrape('https://coronavirus.marinhhs.org/', 5)

### SELECT VARIABLES
positiveCases = soup.body.find("table").find_all('td')[5].contents[0]
updatedAt = deathsRaw = soup.find("div", {"class": "view-footer"}).contents[0]

# Append to JSON File
append('marin', 'N/A', positiveCases, 'N/A', 'N/A', 'N/A')