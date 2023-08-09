"""
Python code to generate sport headlines
phase 2 - convert .py file to an executable to automatically run every time
install - pyinstaller - converts a py file to executable file
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.service import Options
import pandas as pd
from datetime import datetime
import os
import sys

# to export extracted_file in thesame folder the exc file is located
application_path = os.path.dirname(sys.executable)

now = datetime.now()
# DDMMYYYY
date_time = now.strftime("%a%d%m%Y")


website = "https://www.thesun.co.uk/sport/football/"
path = "/chromedriver"

#headless-mode  //modifies defualt behavior of selenium
options = Options()
options.headless = True
# create service, driver and access website
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)



# to extract the title text/s
containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container]')

# to extract and export data into csv file
# create empty lists
titles = []
subtitles = []
links = []

# get text data 
for container in containers:
    title = container.find_element(by="xpath", value='./a/h2').text
    subtitle = container.find_element(by="xpath", value='./a/p').text 
    link = container.find_elements(by="xpath", value='./a').get_attribute("href")

    # append elements to lists
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

# create a dict
my_dict = {'titles' : titles ,
           'subtitles': subtitles,
           'lints' : links}
# create a dataframe
df_headlines = pd.DataFrame(my_dict)
# export data to csv
file_name = f'headline-{date_time}.csv'

final_path = os.path.join(application_path, file_name)

#df_headlines.to_csv('headline.csv')
df_headlines.to_csv(final_path)

driver.quit() 


"""
To use pyinstaller in terminal :
$ pip install pyinstaller
$ pyinstaller --onefile selenium_exc.py
    - locate build and dist folder in root folder
    - dist is the executable folder
    - run exec file in dist folder
"""

