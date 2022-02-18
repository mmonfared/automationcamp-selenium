from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(3)
alert = Alert(driver)
actions = ActionChains(driver)


############## Alert ###############

# 1) Alert - Get text
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
print(alert.text)
sleep(3)

# 2) Alert - Accept
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
sleep(1)
alert.accept()
# driver.find_element(By.XPATH, "//*[text()='You clicked: Ok']")  # or we can check the DOM like following
dom = driver.page_source
assert 'You clicked: Ok' in dom
sleep(3)

# 3) Alert - Dismiss
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
sleep(1)
alert.dismiss()
# driver.find_element(By.XPATH, "//*[text()='You clicked: Cancel']")
dom = driver.page_source
assert 'You clicked: Cancel' in dom
sleep(3)

# 4) Alert - Send text
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
sleep(1)
alert.send_keys("This is AutomationCamp")
alert.accept()
assert "This is AutomationCamp" in driver.page_source
sleep(3)

############## Popup (Dialog) ###############
driver.get("https://material.angular.io/components/dialog/examples")
cdk_button = driver.find_element(By.XPATH, "//*[@class='mat-button-wrapper' and text()='CDK']")
offset = cdk_button.location
driver.find_element(By.XPATH, "//button[@class='mat-focus-indicator mat-button mat-button-base']").click()
# Validations
driver.find_element(By.XPATH, "//h3[text()='Develop across all platforms']")
driver.find_element(By.XPATH, "//button//*[text()='Install']")
driver.find_element(By.XPATH, "//button//*[text()='Cancel']")
# Closing the dialog by click on context
actions.move_by_offset(offset['x'], offset['y']).pause(0.5).click().perform()
driver.find_element(By.XPATH, "//button[@class='mat-focus-indicator mat-button mat-button-base']").click()

############## Snackbar ###############
driver.get("https://material.angular.io/components/snack-bar/examples")
driver.find_element(By.XPATH, "//input[@id='mat-input-0']").clear()
driver.find_element(By.XPATH, "//input[@id='mat-input-0']").send_keys(1)
driver.find_element(By.XPATH, "//*[@class='mat-button-wrapper' and normalize-space(text())='Pizza party']/ancestor::button").click()

# 1:
driver.find_element(By.XPATH, "//*[@class='cdk-overlay-container']//*[contains(text(), 'Pizza party')]")
sleep(3)
print("Test Passed")

# 2:
driver.find_element(By.XPATH, "//*[@class='cdk-overlay-container']/following::*[contains(text(), 'Pizza party')]")

#3:
# - Step 1 - Debug the dom
dom = driver.page_source
print(dom)
# - Step 2
driver.find_element(By.XPATH, "//snack-bar-container")
driver.find_element(By.XPATH, "//snack-bar-container//*[contains(text(), 'Pizza party')]")
sleep(3)
print("Test Passed")

############## Tooltip ###############
def check_tooltip_is_visible(elements: list, check_text):
    for el in elements:
        try:
            text = el.text
            assert text == check_text
            return
        except:
            pass
    raise Exception("Tooltip message cannot found")

driver.get("https://material.angular.io/components/tooltip/examples#tooltip-message")
input_element = driver.find_element(By.XPATH, "//*[@id='mat-input-2']")
input_element.clear()
driver.find_element(By.XPATH, "//*[@id='mat-input-2']").send_keys("AutomationCamp-Session 13")
hover_element = driver.find_element(By.XPATH, "(//button[@class='mat-focus-indicator mat-tooltip-trigger mat-raised-button mat-button-base'])[4]")
actions.move_to_element(hover_element).perform()
tooltip_elements1 = driver.find_elements(By.XPATH, "//*[@class='cdk-overlay-container']/descendant::*")
check_tooltip_is_visible(tooltip_elements1, "AutomationCamp-Session 13")
assert len(tooltip_elements1) > 0
actions.move_to_element(input_element).perform()
tooltip_elements2 = driver.find_elements(By.XPATH, "//*[@class='cdk-overlay-container']/descendant::*")
assert len(tooltip_elements2) == 0
sleep(2)
print("Test is PASSED")
