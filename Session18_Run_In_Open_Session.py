from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


def open_session():
    user_dir = "C:/Users/MM/Documents/AutomationCamp/temp/user_dir"
    options = webdriver.ChromeOptions()
    service = Service(executable_path=ChromeDriverManager().install())
    options.add_argument("--remote-debugging-port=8484")
    options.add_argument(f"--user-data-dir={user_dir}")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def continue_session():
    service2 = Service(executable_path=ChromeDriverManager().install())
    options2 = webdriver.ChromeOptions()
    options2.add_experimental_option("debuggerAddress", "localhost:8484")
    driver2 = webdriver.Chrome(service=service2, options=options2)
    return driver2

driver = open_session()
driver.implicitly_wait(3)
driver.get("http://play2.automationcamp.ir/index.html")
driver.find_element(By.ID, 'fname').send_keys("Mohammad")

driver = continue_session()
driver.find_element(By.XPATH, "//input[@id='male']").click()
driver.find_element(By.ID, "lname").send_keys("Monfared")

sleep(3)

driver.close()
driver.quit()
