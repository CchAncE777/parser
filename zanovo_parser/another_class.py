import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class bebebe:
    def __init__(self, link, start_day, last_day):
        self._link = link
        self._start_day = start_day
        self._last_day = last_day
        self._total_days = (last_day - start_day).days
        self._driver = webdriver.Chrome()
        self._wait = WebDriverWait(self._driver, 10)

    def accept_cookie(self):
        accept_cookie_button = self._wait(
                EC.element_to_be_clickable((By.ID, "submit_personal"))
                )
        accept_cookie_button.click()

    def click_next_day(self):
        for step in range(self._total_days):
            next_day_button = self._wait.until(
                    EC.presence_of_element_located((By.XPATH, "//div[@data-week-calendar-day-index='4']"
                    )))
        
            self._driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_day_button)
        
            actions = ActionChains(self._driver)
            actions.move_to_element(next_day_button).click().perform()