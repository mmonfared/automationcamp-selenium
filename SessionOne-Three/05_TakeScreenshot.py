from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os
from pathlib import Path

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("http://yahoo.com")
sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
current_path = Path(__file__).parent
file_name = os.path.join(str(current_path), 'session2.png')
driver.save_screenshot(file_name)
