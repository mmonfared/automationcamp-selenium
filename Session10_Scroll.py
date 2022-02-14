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
driver.implicitly_wait(2)

################### Scroll Using JavaScript Commands #########################
# Scroll down by pixel
driver.get("https://trytestingthis.netlify.app/")
driver.execute_script("window.scrollBy(0,200)")
sleep(3)

# Scroll to specific position
driver.get("https://trytestingthis.netlify.app/")
driver.execute_script("window.scrollTo(0,500)")

# Scroll to element if could find by driver
driver.get("https://www.imdb.com/chart/top/")
element = driver.find_element('link text', 'The Handmaiden')
print(element)
driver.execute_script("arguments[0].scrollIntoView();", element)
sleep(3)

# Scroll to element if currently cannot be found or not sure if it is in the page (True-False)
def scroll_to_find_element(locator, pixel):
    for i in range(10):
        try:
            driver.find_element(locator[0], locator[1])
            return True
        except:
            driver.execute_script(f"window.scrollBy(0,{str(pixel)})")
            sleep(0.5)
    return False

driver.get("https://www.imdb.com/chart/top/")
result = scroll_to_find_element(['link text', 'fwfwfqgeqrhr'], 1800)
print(result)

# Scroll to element if currently cannot be found or not sure if it is in the page (Assertion)
def scroll_to_find_element(locator, pixel):
    for i in range(10):
        try:
            driver.find_element(locator[0], locator[1])
            print(f"The element '{locator}' has been found")
        except:
            driver.execute_script(f"window.scrollBy(0,{str(pixel)})")
            sleep(0.5)
    raise Exception(f"The element '{locator}' cannot be found")

driver.get("https://www.imdb.com/chart/top/")
scroll_to_find_element(['link text', 'fwfwfqgeqrhr'], 1800)
driver.quit()

# Scroll to down of the page
driver.get("https://www.imdb.com/chart/top/")
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")  #1
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")  #2


# Scroll to top of the page
driver.get("https://www.imdb.com/chart/top/")
driver.execute_script("window.scrollBy(0, 0)")

# Scroll horizontally
driver.get("https://datatables.net/examples/basic_init/scroll_x.html")
driver.execute_script("document.querySelector('table td:last-child').scrollIntoView()")

################### Is displayed #########################
driver.get("https://www.imdb.com/chart/top/")
for i in range(10):
    try:
        result = driver.find_element('link text', 'Andrei Rublev').is_displayed()
    except:
        sleep(0.5)

################### Scroll Using ActionChains #########################
driver.get("https://trytestingthis.netlify.app/")
el1 = driver.find_element('xpath', "//*[@name='message']")
el2 = driver.find_element('id', 'fname')
actions.move_to_element(el2).click_and_hold().move_to_element(el1).release().perform()
sleep(3)

################### Scroll Using Keyboard #########################

# Scroll to End of page and Top of the page
driver.get("https://trytestingthis.netlify.app/")
page_el = driver.find_element('tag name', 'html')
actions.send_keys_to_element(page_el, Keys.END).perform()
sleep(3)
actions.send_keys_to_element(page_el, Keys.HOME).perform()
sleep(3)

# Scroll to find element
driver.implicitly_wait(2)
def scroll_to_find_element(locator):
    page_el = driver.find_element('tag name', 'html')
    for i in range(10):
        try:
            driver.find_element(locator[0], locator[1])
            return True
        except:
            # actions.send_keys_to_element(page_el, Keys.DOWN).perform()
            # actions.send_keys_to_element(page_el, Keys.DOWN).perform()
            # actions.send_keys_to_element(page_el, Keys.DOWN).perform()
            # actions.send_keys_to_element(page_el, Keys.DOWN).perform()
            # actions.send_keys_to_element(page_el, Keys.DOWN).perform()
            actions.send_keys_to_element(page_el, Keys.PAGE_DOWN).perform()
            sleep(0.5)
    return False

################### Scroll Using WebDriver #########################

# Scroll to element
driver.get("https://www.imdb.com/chart/top/")
element = driver.find_element('link text', 'The Handmaiden')
element.location_once_scrolled_into_view
sleep(3)

# Scroll horizontally
driver.get("https://datatables.net/examples/basic_init/scroll_x.html")
driver.set_window_size(480,640)
element = driver.find_element('xpath', '//tbody//td[last()]')
sleep(1)
element.location_once_scrolled_into_view
sleep(3)


