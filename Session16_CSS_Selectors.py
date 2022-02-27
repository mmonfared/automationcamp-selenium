from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.play2.automationcamp.ir/index.html")

# driver.find_element("css selector")
driver.find_element(By.CSS_SELECTOR, "input[id='fname']").send_keys("AutomtionCamp")
sleep(3)
