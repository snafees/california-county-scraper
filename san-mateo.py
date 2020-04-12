# San Mateo County
from bs4 import BeautifulSoup
from scraper_init import scrape
from append import append

# Init Scraper and Return Soup
soup = scrape('https://www.smchealth.org/coronavirus', 5)

# Select Figures
positiveCases_table = soup.find_all("table")[0] #{"clas: "contacts_table"}).div.select('em')[0].contents[0] #alameda
positiveCases = soup.find_all("table")[0].find_all('td')[1].text
deaths = soup.find_all("table")[0].find_all('td')[3].text

# Append to JSON File
append('san_mateo', 'N/A', positiveCases, deaths, 'N/A', 'N/A')
