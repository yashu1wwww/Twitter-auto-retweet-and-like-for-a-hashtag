from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import random


driver= webdriver.Chrome()
driver.maximize_window()

driver.get("https://twitter.com/i/flow/login")
time.sleep(6)
email = driver.find_element_by_name('text')
email.send_keys("twitter") #replace with your twitter username
email.send_keys(Keys.ENTER)
time.sleep(3)
password = driver.find_element_by_name("password")
password.send_keys("twitter123@#") #replace with your twitter password
password.send_keys(Keys.ENTER)
time.sleep(6)
input_field = driver.find_element_by_xpath('//input[@data-testid="SearchBox_Search_Input"]')
input_field.send_keys('#kohli') #replace with hastag which you needed
input_field.send_keys(Keys.ENTER)

# Wait for the search results to load
time.sleep(5)

while True:
    try:
        retweet_button = driver.find_element_by_xpath("//div[@data-testid='retweet']/div").click() #retweet button
        time.sleep(1)
        
        retweet_button = driver.find_element_by_xpath("//div[@data-testid='retweetConfirm']/div").click() #retweet click #confirm
        time.sleep(2)
        
        like_button = driver.find_element_by_xpath("//div[@data-testid='like']/div") #like button
        like_button.click()
        
        time.sleep(2) 
    except NoSuchElementException:
        break  




