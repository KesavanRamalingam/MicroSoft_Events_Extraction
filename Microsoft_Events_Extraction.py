import requests, time, random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd


PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://events.microsoft.com/?timeperiod=all&isSharedInLocalViewMode=false&startTime=&endTime=")


for i in range (329):
    time.sleep(3)
    button = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/main/div[6]/div/input')
    time.sleep(2)
    actions = ActionChains(driver)
    actions.click(button).perform()
    time.sleep(7)

src = driver.page_source
soup = BeautifulSoup(src,'lxml')

parsed_content = soup.find_all('article', {'class': "item grid-group-item col-sm-6 col-xs-6 col-md-3 portrait-width"})

item_list=[]

for i in parsed_content:
    title = i.find('div', {'class': 'eventTitle ng-binding'}).text.strip()
    try:
        time = i.find('div', {'class': 'eventDate ng-binding ng-scope'}).text.strip()
    except:
        time = "Not Found"
    try:
        location = i.find('span', {'ng-bind-html': 'events.LocationName'}).text.strip()
    except:
        location = i.find('div', {'class': 'timeZone ng-binding'}).text.strip()
        
    Highlight = i.find('p', {'class': 'eventDescription ng-binding ng-scope'}).text.strip()
    try:
        url = i.find('a')['href']
    except:
        url = 'Not Found'
        
    items={
        'title':title,
        'time':time,
        'location':location,
        'Highlight':Highlight,
        'url':url,
    }
    
    item_list.append(items)
    
df = pd.DataFrame(item_list)