from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())  # With WebDriver Manager

# Browser Action 1 > Open Web
driver.get("http://google.com")
sleep(1)

# Browser Action 2 > Title
window_title = driver.title
print(window_title)

# Browser Action 3 > Back
driver.get("http://wikipedia.com")
sleep(1)
driver.back()
sleep(1)

# Browser Action 4 > Forward
driver.forward()
sleep(1)

# Browser Action 5 > Refresh
driver.refresh()
sleep(1)

# Browser Action 6 > Open new window and switch to it (Tab)
driver.switch_to.new_window('tab')
sleep(1)

# Browser Action 7 > Open new window and switch to it (window)
driver.switch_to.new_window('window')
driver.get('http://yahoo.com')
sleep(1)

# Browser Action 8 > Current window
yahoo_window = driver.current_window_handle
print('yahoo handle' + str(yahoo_window))

# Browser Action 9 > All handles
all_handle = driver.window_handles
print('all_handles' + str(all_handle))

# Browser Action 10 > Switch
driver.switch_to.window(all_handle[0])
sleep(1)

# Browser Action 11 > Close tab
driver.close()
sleep(1)

# Browser Action 12 > Quit session
# driver.quit()

# Browser Action 13 > Window Size
window_size = driver.get_window_size()  # {'width': 1050, 'height': 796}

# Browser Action 14 > Set Window Size
driver.set_window_size(800, 600)
sleep(1)

# Browser Action 15 > Get window position
current_position = driver.get_window_position()
print(current_position)
sleep(1)

# Browser Action 16 > Set window position
driver.set_window_position(400, 500)
sleep(1)

# Browser Action 17 > minimize window
driver.minimize_window()
sleep(1)

# Browser Action 18 > Maximize window
driver.maximize_window()
sleep(1)

# Browser Action 19 > Full screen window
driver.fullscreen_window()
sleep(1)
