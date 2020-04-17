# San Francisco 
from bs4 import BeautifulSoup
from scraper_init import scrape
from append import append
from notify import send

# Init Scraper and Return Soup
soup = scrape('https://www.sfdph.org/dph/alerts/coronavirus.asp', 10)

try: 
    positiveCasesRaw = soup.find_all("div", {"id": "helpful-links"})[1].p.contents[0]
    deathsRaw = soup.find_all("div", {"id": "helpful-links"})[1].find_all('p')[1].contents[0]
    
    #String Replace
    positiveCasesClean = positiveCasesRaw.replace("Total Positive Cases: ", "")
    deaths = deathsRaw.replace("Deaths: ", "")
    
    
    ### APPEND TO JSON FILE ###
    append('san_francisco', 'N/A', positiveCasesClean, deaths, 'N/A', 'N/A')
except Exception as e:
    send("San Francisco", e)    