from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
import os
# import requests
import time




options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\Admin\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1\\")
# driver = webdriver.Chrome(options=options)
driver = uc.Chrome(options=options)
time.sleep(2)

driver.get('https://quillbot.com')
# driver.minimize_window()
time.sleep(10)

# input_file_path="./answer.txt"
# with open(input_file_path, 'r') as f:
#     content = f.read()

# driver.find_element(By.ID,"inputText").send_keys(content)
# # time.sleep(1)

# driver.find_element(By.XPATH, '//button/parent::div[@class="MuiGrid-root css-rfnosa"]').click()
# time.sleep(10)

# paraphrased_text = driver.find_element(By.XPATH, '//div[@id="outputText"]')

# output_file_path="./parapharased.txt"
# with open(output_file_path, 'w') as f:
#     f.write(paraphrased_text.text)

driver.quit()
