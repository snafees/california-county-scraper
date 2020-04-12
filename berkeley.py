# Berkeley 
from bs4 import BeautifulSoup
from scraper_init import scrape
from append import append

# Init Scraper and Return Soup
soup = scrape('https://www.cityofberkeley.info/coronavirus/', 5)

### SELECT VARIABLES
# positiveCases = soup.find_all('strong')[0].contents[0]
# deaths = "1"
# print(positiveCases)

# Append to JSON File
append('berkeley', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A')
