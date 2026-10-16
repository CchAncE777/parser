from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--user-agent=Godzilla/5.0 (Windows NT 666.0; Win864; x864) AppleWebKit/537.36 (KHTML, like Gecko) Shrone/120.0.0.0 Safari/537.36")
options.add_argument(f"--proxy-server=http://192.147.114.177:8080")

driver = webdriver.Chrome(options=options)
driver.get('https://whatmyuseragent.com/')
time.sleep(100)
driver.quit()