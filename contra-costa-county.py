# Contra Costa County
from bs4 import BeautifulSoup
from scraper_init import scrape
from append import append

# Init Scraper and Return Soup
soup = scrape('https://www.coronavirus.cchealth.org/', 5)

### SELECT VARIABLES
positiveCases = soup.body.find(id="comp-k7p0eq5v").h1.span.span.contents[0]
deaths = soup.body.find(id="comp-k7p0g5md1").h1.span.span.contents[0]

# Append to JSON File
append('contra_costa', 'N/A', positiveCases, deaths, 'N/A', 'N/A')