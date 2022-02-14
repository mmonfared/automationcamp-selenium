from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()

## 1 ##### Without Data-Dir
# user_dir = "C:/Users/MM/Documents/AutomationCamp/automationcamp/user_dir"  # User 1
user_dir = "C:/Users/MM/Documents/AutomationCamp/automationcamp/user_dir_2"  # User 2
options.add_argument(f"user-data-dir={user_dir}")
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://app.clockify.me/signup")
windows = driver.window_handles
driver.switch_to.window(windows[0])
# driver.find_element(By.XPATH, "//input[@type='email']").send_keys("automationcamp@jffwoffjpp.com")  # User 1
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("session14@jffwoffjpp.com")  # User 2
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("123456")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

for i in range(10):
    try:
        driver.find_element(By.ID, 'sidebar-menu')
        break
    except:
        sleep(1)

sleep(3)

## 2 ##### Using Data-Dir
# user_dir = "C:/Users/MM/Documents/AutomationCamp/automationcamp/user_dir"
user_dir = "C:/Users/MM/Documents/AutomationCamp/automationcamp/user_dir_2"  # User 2
options.add_argument(f"user-data-dir={user_dir}")
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://app.clockify.me/tracker")
for i in range(10):
    try:
        driver.find_element(By.ID, 'sidebar-menu')
        break
    except:
        sleep(1)

sleep(4)

## 3 ##### Open without cache, but keep previous cache
user_dir = "C:/Users/MM/Documents/AutomationCamp/automationcamp/user_dir"
options.add_argument(f"user-data-dir={user_dir}")
options.add_argument("--incognito")
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://app.clockify.me/tracker")
sleep(4)



