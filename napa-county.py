# Napa County
from bs4 import BeautifulSoup
from scraper_init import scrape
from append import append
from notify import send

# Init Scraper and Return Soup
soup = scrape('https://legacy.livestories.com/s/v2/coronavirus-report-for-napa-county-ca/9065d62d-f5a6-445f-b2a9-b7cf30b846dd/', 10)

try: 
    ### SELECT VARIABLES
    selection = soup.body.find_all("table")[0].find_all("tr")[1].find_all("td")
    positiveCases = selection[1].contents[0]
    deaths = selection[2].contents[0]
    
    # Append to JSON File
    append('napa', 'N/A', positiveCases, deaths, 'N/A', 'N/A')
except Exception as e:
    send("Napa", e)    


