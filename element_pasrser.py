import time
import selenium
import os
import random
from PIL import Image , ImageEnhance
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

class Parser:
    def __init__(self, link):
        self.link = link
        self.driver = webdriver.Firefox()
        self.driver.get(self.link)
        self.info_list = []
        self.links_list = [] 

    def get_links_on_page(self):
        elements = self.driver.find_elements(By.CLASS_NAME, 'c-list__center')
        for element in elements:
            link = element.find_element(By.TAG_NAME, 'a')
            self.links_list.append(link.get_attribute('href'))

    def go_to_the_next_page(self):
        clickable_element = WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/div/div[1]/div[3]/div[3]/a"))
        )
        self.driver.execute_script("arguments[0].click();", clickable_element)

    def accept_cookie(self):
        clickable_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "popup-cookie__confirm"))
        )
        clickable_element.click()

    def get_info(self):
        for link in self.links_list[:7]:
            self.driver.get(link + "#characteristics")
            time.sleep(6)
            # wait = WebDriverWait(self.driver, 10)
            # wait.until(EC.any_of((By.CLASS_NAME, "prod-tab-specifications__table")))
            tabble_list = self.driver.find_elements(By.CLASS_NAME, 'prod-tab-specifications__table')
            for table in tabble_list:
                self.info_list.append(table.text)
            time.sleep(3)

    def __del__ (self):
        print("zakoncheno")
