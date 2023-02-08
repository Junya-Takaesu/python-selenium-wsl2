import time
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")

# Step 3: Install compatible Chromedriver を飛ばしたので、
# 以下の２行は不要。
# homedir = os.path.expanduser("~")
# webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")

# Step 3: Install compatible Chromedriver を飛ばしたので、
# 以下の行は不要。
# browser = webdriver.Chrome(service=webdriver_service,options=chrome_options)
browser = webdriver.Chrome(options=chrome_options)
browser.get("https://cloudbytes.dev")
description = browser.find_element(By.NAME, "description").get_attribute("content")
print(f"{description}")

time.sleep(10)
browser.quit()