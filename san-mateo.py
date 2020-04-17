# San Mateo County
from bs4 import BeautifulSoup
from scraper_init import scrape
from append import append


# Init Scraper and Return Soup
soup = scrape('https://app.powerbigov.us/view?r=eyJrIjoiODZkYzM4MGYtNDkxNC00Y2ZmLWIyYTUtMDNhZjlmMjkyYmJkIiwidCI6IjBkZmFmNjM1LWEwNGQtNDhjYy1hN2UzLTZkYTFhZjA4ODNmOSJ9', 5)

try: 
    # Select Figures
    select = soup.find_all("text")
    containers = soup.find_all("visual-container-modern")
    positiveCases = select[0].find("title").contents[0]
    deaths = containers[8].find_all("text")[0].find("title").contents[0]
    
    # Append to JSON File
    append('san_mateo', 'N/A', positiveCases, deaths, 'N/A', 'N/A')
except Exception as e:
    send("San Mateo", e)    