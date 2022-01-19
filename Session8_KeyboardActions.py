from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
actions = ActionChains(driver=driver)

driver.maximize_window()
driver.get("http://google.com")
search_box = driver.find_element('name', 'q')

# Type
search_box.send_keys("Selenium")

# Type + ENTER
search_box.send_keys("selenium" + Keys.ENTER)

# Select All (key_down)
actions.key_down(Keys.CONTROL).send_keys('a').perform()

# Holding Shift + type
actions.key_down(Keys.SHIFT).send_keys_to_element(search_box, 'selenium').perform()

# key_up()
actions.key_down(Keys.SHIFT).send_keys_to_element(search_box, 'selenium').key_up(Keys.SHIFT).send_keys(" selenium").perform()

# Clear field using clear()
search_box.clear()

# Clear field using CTRL+A+Del
search_box.click()
actions.key_down(Keys.CONTROL).send_keys('a').send_keys(Keys.DELETE).perform()
