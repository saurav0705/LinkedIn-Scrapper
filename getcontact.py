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

driver = webdriver.Chrome('C:\\Users\\saurav.aggarwal\\Desktop\\chromedriver')
driver.get('https://www.google.com/maps/place/KNOWLEDGE+RIDGE+PVT+LTD/@18.5403127,73.8968582,15z/data=!4m5!3m4!1s0x0:0x18b88a2d575c94b4!8m2!3d18.5403127!4d73.8968582')


INPUT_XPATH = '/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/form/div/div[3]/div/input[1]'
WIDGET_PATH = '/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[8]'
SEARCH_XPATH = '/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]'
XPATH = '//*[@id="pane"]/div/div[1]/div/div/div[8]/div/div[1]/span[3]/span[3]'
CONTACT_XPATH = '//*[@id="pane"]/div/div[1]/div/div/div[11]/div/div[1]/span[3]/span[3]'
fl = open('companies_glassdoor_contact.txt','r+')
x = fl.read()
'''//*[@id="pane"]/div/div[1]/div/div/div[8]/div/div[1]/span[3]'''

time.sleep(10)
for comp in x.split("\n"):

    inp = driver.find_element_by_xpath(INPUT_XPATH)
    inp.click()
    inp.clear()
    inp.send_keys(comp+" pune")
    inp.send_keys(Keys.ENTER)
    time.sleep(10)
    print(comp + "-----------")
    try:
        el = driver.find_element_by_xpath(CONTACT_XPATH)
        # print(el.get_attribute('innerHTML'))
        soup = BeautifulSoup(el.get_attribute('innerHTML'), "html.parser")
        lst = []
        span = soup.findAll('span')
        
        lst.append(str(soup))
        with open('data_contact.txt', 'a+') as outfile:
            json.dump({comp : str(soup)},outfile,indent=4)
        lst = []


        # if(len(lst) == 0 ):
        #     try:
        #         el = driver.find_element_by_xpath(XPATH)
        #         soup = BeautifulSoup(el.get_attribute('innerHTML'), "html.parser")
        #         lst = []
        #         span = soup.findAll('span')
        #         for s in soup:
        #             lst.append(div.getText())
        #         with open('data_address.txt', 'a+') as outfile:
        #             json.dump({comp:lst},outfile,indent=4)
        #         lst = []
        #     except:
        #         print("not found")
        #         with open('data_address.txt', 'a+') as outfile:
        #             json.dump({comp:[]},outfile,indent=4)
        #         lst = []
        # else:
        #     with open('data_address.txt', 'a+') as outfile:
        #         json.dump({comp:lst},outfile,indent=4)
        # lst = []
    except Exception as e:
        print(e)
        with open('data_contact.txt', 'a+') as outfile:
            json.dump({comp:[]},outfile,indent=4)
        


driver.quit()