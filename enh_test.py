from PIL import Image, ImageEnhance

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

def enhance_pic(image_path):
    image = Image.open(f"{image_path}")

    if image.mode != "RGB":
        image = image.convert("RGB")

    brightness_factor = 1.2
    enhancer_b = ImageEnhance.Brightness(image)
    bright_img = enhancer_b.enhance(brightness_factor)

    contrast_factor = 1.5
    enhancer_c = ImageEnhance.Contrast(bright_img)
    final_img = enhancer_c.enhance(contrast_factor)

    final_img = final_img.convert('1')
    final_img.save("pics/result_pillow.png")

enhance_pic(image_path)