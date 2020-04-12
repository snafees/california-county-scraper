# Alameda County
from bs4 import BeautifulSoup
from scraper_init import scrape
from append import append

# Init Scraper and Return Soup
soup = scrape('https://ac-hcsa.maps.arcgis.com/apps/opsdashboard/index.html#/948c67558cff414dbbee1a78fcbab1c9', 5)

# Select Figures
# positiveCasesRaw = soup.find("full-container").findAll("div")[4]
# print(positiveCasesRaw)

# Append to JSON File
append('alameda', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A')