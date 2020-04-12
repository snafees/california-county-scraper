# Santa Clara County
from bs4 import BeautifulSoup
from scraper_init import scrape
from append import append

# Init Scraper and Return Soup
soup = scrape('https://app.powerbigov.us/view?r=eyJrIjoiZTg2MTlhMWQtZWE5OC00ZDI3LWE4NjAtMTU3YWYwZDRlOTNmIiwidCI6IjBhYzMyMDJmLWMzZTktNGY1Ni04MzBkLTAxN2QwOWQxNmIzZiJ9', 5)

# Select Figures
# positiveCases = soup.find_all("text", {"class": "value"})[0].title.contents[0]
# newCases = soup.find_all("text", {"class": "value"})[1].title.contents[0]
# deaths = soup.find_all("text", {"class": "value"})[2].title.contents[0]

# Append to JSON File
# append('santa_clara', 'N/A', positiveCases, deaths, 'N/A', 'N/A')