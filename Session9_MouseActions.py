from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(3)
actions = ActionChains(driver)

# Click
driver.get("https://trytestingthis.netlify.app/")
driver.find_element("id", "male").click()

# Double Click
driver.get("https://trytestingthis.netlify.app/")
el = driver.find_element('xpath', "//button[text()='Double-click me']")
actions.double_click(el)
actions.perform()
driver.find_element("xpath", "//*[text()='Your Sample Double Click worked!']")
sleep(2)

# Right Click
driver.get("https://trytestingthis.netlify.app/")
el = driver.find_element('id', 'fname')
actions.context_click(el).perform()
sleep(3)

# Move the cursor
driver.get("https://trytestingthis.netlify.app/")
el = driver.find_element('xpath', "//*[@class='tooltip']")
actions.move_to_element(el).perform()
sleep(3)

# Click and Hold
driver.get("https://demos.telerik.com/kendo-ui/circular-gauge/index")
driver.find_element('id', 'onetrust-accept-btn-handler').click()
driver.execute_script("scroll(0,400)")
el = driver.find_element("xpath", "//*[contains(@class, 'k-button-increase')]")
actions.click_and_hold(el).perform()
sleep(3)

# Pause and release
driver.get("https://demos.telerik.com/kendo-ui/circular-gauge/index")
driver.find_element('id', 'onetrust-accept-btn-handler').click()
driver.execute_script("scroll(0,400)")
el = driver.find_element("xpath", "//*[contains(@class, 'k-button-increase')]")
el2 = driver.find_element("xpath", "//*[contains(@class, 'k-button-decrease')]")
actions.click_and_hold(el).pause(3).release().click_and_hold(el2).pause(4).perform()

# Drag and Drop (1)
driver.get("https://selenium08.blogspot.com/2020/01/drag-drop.html")
el1 = driver.find_element('id', 'draggable')
el2 = driver.find_element('id', 'droppable')
actions.move_to_element(el1).click_and_hold().move_to_element(el2).release().perform()
sleep(2)

# Drag and Drop (2)
driver.get("https://selenium08.blogspot.com/2020/01/drag-drop.html")
el1 = driver.find_element('id', 'draggable')
el2 = driver.find_element('id', 'droppable')
actions.drag_and_drop(el1, el2).perform()
sleep(2)

# Get Coordinates
driver.get("https://trytestingthis.netlify.app/")
offset = driver.find_element("xpath", "//*[text()='Lets you select only one option']").location

# Move by offset
driver.execute_script("scroll(0,500)")
sleep(1)
driver.find_element("id", 'option').click()
actions.move_by_offset(offset['x'], offset['y']).pause(1).click().perform()
sleep(3)

# Drag and Drop by Offset
driver.get("https://selenium08.blogspot.com/2020/01/drag-drop.html")
el1 = driver.find_element('id', 'draggable')
el2 = driver.find_element('id', 'droppable')
coord_el1 = driver.find_element('id', 'draggable').location
coord_el2 = driver.find_element('id', 'droppable').location
print("Coord1: " + str(coord_el1))
print("Coord2: " + str(coord_el2))
offset_x = (coord_el2['x'] - coord_el1['x']) + (el2.rect['width']-el1.rect['width'])/2
offset_y = (coord_el2['y'] - coord_el1['y']) + (el2.rect['height']-el1.rect['height'])/2
actions.drag_and_drop_by_offset(el1, offset_x, offset_y).pause(1).perform()
sleep(2)
