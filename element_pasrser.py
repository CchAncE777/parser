from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
import matplotlib.pyplot as plt
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os

class elementParser():
    def __init__(self, element_link):
        self.element_link = element_link
        self.driver = webdriver.Chrome()
        self.driver.get(self.element_link)
        self.info_list = []
        self.links_list = []

    def get_links(self):
        elements = self.driver.find_elements(By.CLASS_NAME, 'c-list__title')
        for element in elements:
            self.links_list.append(element.get_attribute('href'))

    def go_to_next_page(self):
        clickable_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "show-more"))
        )
        self.driver.execute_script("arguments[0].click();", clickable_element)

    def accept_cookie(self):
        element_cookie = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "popup-cookie__confirm"))
        )
        element_cookie.click()

    def get_info(self):
        for link in self.links_list[:20]:
            self.driver.get(link + "#characteristics")
            wait = WebDriverWait(self.driver, 10)
            tables_list = wait.until(EC._element_if_visible(By.CLASS_NAME, "prod-tab-specifications__table"))
            for table in tables_list:
                self.info_list.append(table.text)
            time.sleep(3)
        return self.info_list

    def __del__(self):
        print('Закончено')
