from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(2)

# 1 - 'By' Class
driver.find_element(By.XPATH)
driver.find_element(By.ID)

# 2 - Get Text
driver.get("https://material.angular.io/components/categories")
el = driver.find_element(By.CLASS_NAME, 'mat-button-wrapper')
attr = el.text
print(attr)
# text = driver.find_element(By.CLASS_NAME, 'mat-button-wrapper').text
# print(text)

# 3 - Get Link, Class, ID, ...
el = driver.find_element(By.XPATH, "//*[@class='mat-button-wrapper' and text()='Components']/..")
attr = el.get_attribute('class')
assert 'selected' in attr, 'Element is not selected'
print(attr)
el2 = driver.find_element(By.XPATH, "//*[@class='mat-button-wrapper' and text()='CDK']/..").click()
sleep(1)
attr2 = el.get_attribute('class')
print(attr2)
assert 'selected' not in attr2, 'Element is selected'
sleep(3)

# 4 - Radio Button
driver.get("https://material.angular.io/components/slide-toggle/examples")
el_accent = driver.find_element(By.ID, 'mat-radio-3')
assert 'checked' in el_accent.get_attribute('class')
el = driver.find_element(By.ID, 'mat-radio-2')
attr1 = el.get_attribute('class')
print(attr1)
assert 'checked' not in attr1
sleep(1)

el.click()
attr2 = el.get_attribute('class')
print(attr2)
assert 'checked' in attr2
assert 'checked' not in el_accent.get_attribute('class')
sleep(3)

# 5 - Switch Button
driver.get("https://material.angular.io/components/slide-toggle/examples")
toggle = driver.find_element(By.ID, 'mat-slide-toggle-1')
assert 'checked' not in toggle.get_attribute('class')
sleep(1)
toggle.click()
assert 'checked' in toggle.get_attribute('class')

# 6 - Checkbox
assert 'disabled' not in toggle.get_attribute('class') # 7 - Enable/Disable
checkbox = driver.find_element(By.ID, 'mat-checkbox-2')
assert 'checked' not in checkbox.get_attribute('class')
sleep(1)
driver.find_element(By.XPATH, "//*[text()='Ok, Got it']").click()
checkbox.click()
assert 'checked' in checkbox.get_attribute('class')

# 7 - Enable/Disable
assert 'disabled' in toggle.get_attribute('class')

# 8 - Get value of input
driver.get("https://material.angular.io/components/input/examples#input-error-state-matcher")
sleep(1)

el = driver.find_element(By.ID, 'mat-input-1')
el.send_keys("This is session 11")
sleep(1)
input_value = el.get_attribute('value')
print(input_value)
assert input_value == "This is session 11"
sleep(3)

# 9 - Input Field Errors
driver.get("https://material.angular.io/components/input/examples#input-error-state-matcher")
sleep(1)
parent_el = driver.find_element(By.XPATH, "//*[@id='mat-input-1']/ancestor::mat-form-field")
assert 'dirty' not in parent_el.get_attribute('class')
input_el = driver.find_element(By.ID, 'mat-input-1').send_keys("sklhfuefhie")
sleep(1)
assert 'dirty' in parent_el.get_attribute('class')