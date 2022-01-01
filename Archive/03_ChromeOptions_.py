from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os
from pathlib import Path
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)   # with chrome options

driver.get("http://yahoo.com")
sleep(3)
