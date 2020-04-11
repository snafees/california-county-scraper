# -*- coding: utf-8 -*-
import json
from datetime import date

### APPEND TO JSON FILE ###
def append(county, totalCases, active, deaths, recovered, tests):
    with open('./scrape.txt', 'r+') as json_file: 
        data = json.load(json_file) 
          
        temp = data[county] 
      
        y = {
             "date": str(date.today()), 
             "total-cases": totalCases,
             "active-cases": active,
             "deaths": deaths, 
             "recovered": recovered,
             "tests": tests
            } 
      
        temp.append(y) 
        json_object = json.dumps(data, indent=4)
        with open("./scrape.txt", "w") as outfile: 
            outfile.write(json_object) 
        #print(json_object)
    #write_json(data)  
   
### EXAMPLE    
# append('sonoma', 15, 'N/A', 'N/A', 'N/A', 'N/A')    
