from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

####### 1) Switch to frame
driver.get("https://www.python.org/dev/peps/")
sleep(2)
driver.switch_to.frame("twitter-widget-0")   # Select by ID/Name
driver.find_element(By.XPATH, "//span[@title='Python Package Index']").click()
sleep(3)
print("PASS")

##  Select frames to switch

# ID or Name
driver.switch_to.frame("twitter-widget-0")
# Index
driver.switch_to.frame(0)   # First
driver.switch_to.frame(1)   # Second
# iframes elements list
iframes = driver.find_elements(By.TAG_NAME, 'iframe')
driver.switch_to.frame(iframes[0])

#######  2) Switch to Default content (Main page)
driver.get("https://www.python.org/dev/peps/")
sleep(2)
driver.switch_to.frame("twitter-widget-0")   # Select by ID/Name
driver.find_element(By.XPATH, "//span[@title='Python Package Index']")
driver.switch_to.default_content()
driver.find_element(By.ID, 'about').click()
sleep(3)
assert "About Python" in driver.title
print("PASS")

#######  3) Parent Frame
driver.get("https://www.play1.automationcamp.ir/frames.html")
sleep(1)
driver.switch_to.frame('frame1')
driver.find_element('id', 'click_me_1').click()
sleep(1)
driver.switch_to.frame('frame2')
driver.find_element('id', 'click_me_2').click()
sleep(1)
print("PASS1")

driver.switch_to.parent_frame()  # Parent frame of current frame
driver.switch_to.frame('frame3')
driver.switch_to.frame('frame4')
driver.find_element('id', 'click_me_4').click()
sleep(1)
print("PASS2")

# 4) Find frame of element

def get_frame_of_element(selector, locator, _driver):
    all_frames = _driver.find_elements(By.TAG_NAME, 'iframe')
    for frame in all_frames:
        _driver.switch_to.frame(frame)
        try:
            _driver.find_element(selector, locator)
            _driver.switch_to.default_content()
            return frame
        except:
            pass
    raise Exception("Could not find the element in all frames")

driver.get("https://www.python.org/dev/peps/")
sleep(2)
frame = get_frame_of_element(By.XPATH, "//span[@title='Python Package Index']", driver)
driver.switch_to.frame(frame)
driver.find_element(By.XPATH, "//span[@title='Python Package Index']").click()
sleep(3)
print("PASS")
