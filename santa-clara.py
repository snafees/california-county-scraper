# Santa Clara County
from bs4 import BeautifulSoup
from scraper_init import scrape
from append import append

# Init Scraper and Return Soup
soup = scrape('https://app.powerbigov.us/view?r=eyJrIjoiZTg2MTlhMWQtZWE5OC00ZDI3LWE4NjAtMTU3YWYwZDRlOTNmIiwidCI6IjBhYzMyMDJmLWMzZTktNGY1Ni04MzBkLTAxN2QwOWQxNmIzZiJ9', 5)

try: 
    # Select Figures
    select = soup.find_all("text")
    containers = soup.find_all("visual-container-modern")
    positiveCases = containers[2].find("title").contents[0]
    deaths = containers[18].find_all("text")[0].find("title").contents[0]
    
    # Append to JSON File
    append('santa_clara', 'N/A', positiveCases, deaths, 'N/A', 'N/A')
except Exception as e:
    send("Santa Clara", e) 