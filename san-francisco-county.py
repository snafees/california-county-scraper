# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import simplejson as json
from datetime import date

### SCRAPE ###

url = "https://www.sfdph.org/dph/alerts/coronavirus.asp"
page = requests.get(url)
contents = page.content
soup = BeautifulSoup(contents, 'html.parser')

positiveCasesRaw = soup.find_all("div", {"id": "helpful-links"})[1].p.contents[0]
deathsRaw = soup.find_all("div", {"id": "helpful-links"})[1].find_all('p')[1].contents[0]

#String Replace
positiveCasesClean = positiveCasesRaw.replace("Total Positive Cases: ", "")
deaths = deathsRaw.replace("Deaths: ", "")

def write_json(data, filename='scrape.txt'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 
      
  
### APPEND TO JSON FILE ###  
    
with open('./scrape.txt') as json_file: 
    data = json.load(json_file) 
      
    temp = data['san-francisco'] 
  
    # python object to be appended 
    y = {
         "date": str(date.today()), 
         "deaths": deaths, 
         "positive-cases": positiveCasesClean
        } 
  
    # print(y)
    # appending data to emp_details  
    temp.append(y) 
    print(temp)
      
write_json(data)  