from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
actions = ActionChains(driver)
driver.implicitly_wait(1)

# 1 - Sleep
print(datetime.now())
sleep(3)
print(datetime.now())
#######################################################

# 2 - Implicitly Wait
driver.get("https://play1.automationcamp.ir/index.html")
driver.implicitly_wait(3)
print(datetime.now())
try:
    driver.find_element(By.XPATH, "//*[text()='sjguiafhipe']")
except:
    print(datetime.now())


#######################################################

# 3 - Wait until element has an attribute
def wait_until_element_has_an_attribute(element_selector, element_locator, attribute, attribute_value, timeout=5,
                                        exact=True):
    for i in range(timeout * 5):
        try:
            element = driver.find_element(element_selector, element_locator)
            if exact:
                assert element.get_attribute(attribute) == attribute_value
            else:
                assert attribute_value in element.get_attribute(attribute)
            print(" Element attribute met: " + str(attribute_value))
            return
        except:
            sleep(0.2)
    raise Exception("Element attribute is not: " + str(attribute_value))


# 4 - Wait until element has not an attribute
def wait_until_element_has_not_an_attribute(element_selector, element_locator, attribute, attribute_value, timeout=5,
                                            exact=True):
    for i in range(timeout * 5):
        try:
            element = driver.find_element(element_selector, element_locator)
            if exact:
                assert element.get_attribute(attribute) != attribute_value
            else:
                assert attribute_value not in element.get_attribute(attribute)
            print(" Element attribute not in or not equals: " + str(attribute_value))
            return
        except:
            sleep(0.2)
    raise Exception("Element attribute in or equals: " + str(attribute_value))


driver.get("https://www.play1.automationcamp.ir/expected_conditions.html")
trigger = driver.find_element(By.ID, "enabled_trigger")
trigger.location_once_scrolled_into_view
wait_until_element_has_an_attribute(By.ID, "enabled_target", 'class', 'danger', exact=False)
wait_until_element_has_not_an_attribute(By.ID, "enabled_target", 'class', 'success', exact=False)
trigger.click()
wait_until_element_has_an_attribute(By.ID, "enabled_target", 'class', 'success', exact=False)
wait_until_element_has_not_an_attribute(By.ID, "enabled_target", 'class', 'danger', exact=False)
print("Test case PASSED")


#######################################################

# 5 - Wait until element is enabled
def wait_until_element_is_enabled(selector, locator, timeout):
    for i in range(timeout * 2):
        try:
            element = driver.find_element(selector, locator)
            assert element.is_enabled()
            return
        except:
            sleep(0.5)


# 6 - Wait until element is not enabled
def wait_until_element_is_not_enabled(selector, locator, timeout):
    for i in range(timeout * 2):
        try:
            element = driver.find_element(selector, locator)
            assert not element.is_enabled()
            return
        except:
            sleep(0.5)


driver.get("https://www.play1.automationcamp.ir/expected_conditions.html")
trigger = driver.find_element(By.ID, "enabled_trigger")
trigger.location_once_scrolled_into_view
trigger.click()
wait_until_element_is_enabled(By.ID, "enabled_target", 5)
print("Element is enabled now!")


#######################################################

# 7 - Wait until element is visible
def wait_until_element_is_visible(selector, locator, timeout=5):
    for i in range(timeout * 2):
        try:
            element = driver.find_element(selector, locator)
            assert element.is_displayed()
            print("Test is PASSED")
            return
        except:
            sleep(0.5)


# 8 - Wait until element is not invisible
def wait_until_element_is_not_visible(selector, locator, timeout=5):
    for i in range(timeout * 2):
        try:
            element = driver.find_element(selector, locator)
            assert not element.is_displayed()
            print("Test is PASSED")
            return
        except:
            sleep(0.5)


driver.get("https://www.play1.automationcamp.ir/expected_conditions.html")
trigger = driver.find_element(By.ID, "visibility_trigger")
trigger.location_once_scrolled_into_view
print(driver.find_element(By.ID, "visibility_target").is_displayed())
trigger.click()
wait_until_element_is_visible(By.ID, "visibility_target")
print(driver.find_element(By.ID, "visibility_target").is_displayed())
#######################################################

# 9 - WebDriverWait until/until not Expected Conditions
driver.get("https://www.play1.automationcamp.ir/expected_conditions.html")
trigger = driver.find_element(By.ID, "enabled_trigger")
trigger.location_once_scrolled_into_view
trigger.click()
wait = WebDriverWait(driver, 5)
element = wait.until(EC.element_to_be_clickable((By.ID, "enabled_target")))
print(element)


#######################################################

# 10 - Wait until page is loaded

def wait_until_page_is_loaded(timeout=10):
    for i in range(timeout * 2):
        try:
            state = driver.execute_script("return document.readyState")
            assert state == 'complete'
            print("State is: " + str(state))
            return
        except:
            sleep(0.5)


driver.get("https://archive.org/details/audio_bookspoetry")
wait_until_page_is_loaded()
