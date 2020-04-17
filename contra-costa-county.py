# Contra Costa County
from bs4 import BeautifulSoup
from scraper_init import scrape
from append import append
from notify import send

# Init Scraper and Return Soup
soup = scrape('https://www.coronavirus.cchealth.org/', 5)

try: 
    ### SELECT VARIABLES
    selection = soup.body.find_all('h1')
    positiveCases = selection[0].contents[0]
    deaths = selection[3].contents[0]
    tests = selection[1].contents[0]
    
    # Append to JSON File
    append('contra_costa', 'N/A', positiveCases, deaths, 'N/A', tests)
except Exception as e:
    send("Contra Costa", e)