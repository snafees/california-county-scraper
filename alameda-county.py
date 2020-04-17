# Alameda County
from bs4 import BeautifulSoup
from scraper_init import scrape
from append import append
from notify import send

# Init Scraper and Return Soup
soup = scrape('https://ac-hcsa.maps.arcgis.com/apps/opsdashboard/index.html#/948c67558cff414dbbee1a78fcbab1c9', 5)

try: 
    # Select Figures
    selection = soup.find("full-container").findAll("div")
    positiveCasesRaw = selection[11].findAll("text")[0].contents[0]
    deaths = selection[19].findAll("text")[0].contents[0]
    
    # Append to JSON File
    append('alameda', positiveCasesRaw, 'N/A', deaths, 'N/A', 'N/A')
except Exception as e:
    send("Alameda", e)