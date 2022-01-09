from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("http://yahoo.com")
sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(2)
