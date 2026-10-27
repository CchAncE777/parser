import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('https://belavia.by/booking/#/results/11356009897')
time.sleep(5)

wait = WebDriverWait(driver, 10)

cookie_button = wait.until(
        EC.element_to_be_clickable((By.ID, "submit_personal"))
        )
cookie_button.click()
time.sleep(15)

current_date = datetime.date(2026, 10, 28)
end_date = datetime.date(2027, 1, 1)
total_days = (end_date - current_date).days

for step in range(total_days):
        next_day_button = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@data-week-calendar-day-index='4']"
                )))
        
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_day_button)
        
        actions = ActionChains(driver)
        actions.move_to_element(next_day_button).click().perform()
        
driver.quit()