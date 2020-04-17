# Marin County
from bs4 import BeautifulSoup
from scraper_init import scrape
from append import append
from notify import send

# Init Scraper and Return Soup
soup = scrape('https://coronavirus.marinhhs.org/', 5)

try: 
    ### SELECT VARIABLES
    positiveCases = soup.body.find("table").find_all('td')[5].contents[0]
    print(positiveCases)
    
    # Append to JSON File
    append('marin', 'N/A', positiveCases, 'N/A', 'N/A', 'N/A')
except Exception as e:
    send("Marin", e)    