from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())  # With WebDriver Manager

driver.get("http://google.com")
sleep(2)
driver.find_element('name', 'q').send_keys("Wikipedia")
sleep(3)
driver.quit()  # TearDown
