# Berkeley 
from bs4 import BeautifulSoup
from scraper_init import scrape
from append import append
from notify import send

# Init Scraper and Return Soup
soup = scrape('https://www.cityofberkeley.info/coronavirus/', 5)

try: 
    ### SELECT VARIABLES
    positiveCases = soup.find_all('strong')[0].contents[0]
    deaths = soup.find_all('strong')[1].contents[0]
    
    # Append to JSON File
    append('berkeley', positiveCases, 'N/A', deaths, 'N/A', 'N/A')
except Exception as e:
    send("Berkeley", e)