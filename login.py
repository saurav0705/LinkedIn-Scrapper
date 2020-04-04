
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import json
from bs4 import BeautifulSoup
import re

import time


driver = webdriver.Chrome('link to chromedriver')


driver.get('https://www.linkedin.com')

time.sleep(5)
username = driver.find_element_by_name('session_key')
username.click()
username.send_keys('your email address')


time.sleep(2)
password = driver.find_element_by_name('session_password')
password.click()
password.send_keys('your password')
time.sleep(2)

sign_in_button = driver.find_element_by_xpath('/html/body/nav/section[2]/form/div[2]/button')

sign_in_button.click()


fl = open('test.txt','r+')
x = fl.read()
print(x.split("\n"))
URL_people = 'https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22in%3A7350%22%5D&keywords=hr%20at%20knowledge%20ridge&origin=GLOBAL_SEARCH_HEADER'
driver.get(URL_people)
SEARCH_CONTAINER = '//*[@id="ember71"]'
LIST_CONTAINER = '//*[@id="ember71"]/div/ul'
CLASS_LIST ='search-result search-result__occluded-item ember-view'
master_list =[]
for comp in x.split("\n"):
    
    time.sleep(5)
    Search_XPATH ='/html/body/header/div/form/div/div/div/div/div[1]/div/input'
    el = driver.find_element_by_xpath(Search_XPATH)
    el.click()
    time.sleep(2)
    el.clear()
    el.send_keys('hr at '+comp)
    time.sleep(2)
    el.send_keys(Keys.ENTER)
    time.sleep(10)

    try:
        data = driver.find_element_by_xpath(SEARCH_CONTAINER).get_attribute('innerHTML')
        soup = BeautifulSoup(data, "html.parser")
        lst = []
        for l in soup.find_all('li'):
            if comp in l.getText():
                lst.append(re.split(r'\s{3,}', l.getText().strip()))
        print(lst)
        master_list.append({comp:lst})
        with open('data_test.txt', 'a') as outfile:
            json.dump({comp:lst},outfile,indent=4)
    except Exception as e:
        print(e)
        master_list.append({comp:[]})
        with open('data_test.txt', 'a') as outfile:
            json.dump({comp:['except ran']},outfile,indent=4)
    print(master_list)



        
driver.quit()
        




