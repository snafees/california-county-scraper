# -*- coding: utf-8 -*-

### SCRAPER INIT
# delay is a required parameter. Many sites are generated dynamically and need a few seconds to load. 

def scrape(url, delay):
    # Imports. Make sure webdriver is executable by running 'chmod +x ./chromedriver' in directory
    from selenium import webdriver
    from bs4 import BeautifulSoup
    import time
    
    ### ENVIRONMENT
    # Update this variable to reflect your environment
    env = 'dev'
    
    ### PRODUCTION
    # Running on EC2
    if env == 'prod':
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(chrome_options=options)
        driver.get(url)
        time.sleep(delay)
        html = driver.page_source
        soup = BeautifulSoup(html, features="html.parser")
    
    ### DEVELOPMENT
    # Running on your local machine
    elif env == 'dev':
        driver = webdriver.Chrome('./chromedriver')
        driver.get(url)
        time.sleep(delay)
        html = driver.page_source
        soup = BeautifulSoup(html, features="html.parser")
    
    driver.quit()
    return soup
    
         
        