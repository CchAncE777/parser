import os
import time
import requests
import tempfile

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from change import enhance_pic

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

driver.get('https://issaold.beltelecom.by/main.html')

image = driver.find_element(By.ID, 'capcher').get_attribute('src')
r_image = requests.get(image)

with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
    temp_file.write(r_image.content)
    image_path = temp_file.name

enhance_pic(image_path)
driver.get('https://www.prepostseo.com/ru/image-to-text')

input = driver.find_element(By.ID, 'uploadFile')
time.sleep(2)
pathhh = "pics/result_pillow.png"
absolute_path = os.path.abspath(pathhh)
input.send_keys(absolute_path)

upload_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Извлечь текст']")))
upload_button.click()

input_text = wait.until(EC.visibility_of_element_located((By.ID, 'result__text0'))).text

driver.get('https://issaold.beltelecom.by/main.html')
text_input = driver.find_element(By.ID, 'cap_field')
text_input.send_keys(input_text)
time.sleep(10)

# check_button = driver.find_element(By.XPATH, '//*[text()="Проверить"]')
# check_button.click()
time.sleep(10)

os.remove(absolute_path)