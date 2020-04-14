# Sonoma County
from bs4 import BeautifulSoup
from scraper_init import scrape
from append import append
from notify import send

# Init Scraper and Return Soup
soup = scrape('https://12356dsf.com/', 1)

# Select Figures

try: 
    content = soup.findAll("table", {"class": "cvTable"})[0].findAll("td")
    totalCases = content[0].contents[0]
    activeCases = content[1].contents[0]
    recoveredCases = content[2].contents[0]
    deaths = content[3].contents[0]
    tests = content[4].contents[0]
    
    # Append to JSON File
    append('sonoma', totalCases, activeCases, deaths, recoveredCases, tests)
except Exception as e:
    send("Sonoma", e)