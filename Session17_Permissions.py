from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

service = Service(executable_path=ChromeDriverManager().install())
options = Options()

# 0 > Ask , 1 > Allow , 2 > Deny
prefs = {
    "profile.default_content_setting_values.geolocation": 2,  # Geo Location
    "profile.default_content_setting_values.media_stream_camera": 1,  # Camera
    "profile.default_content_setting_values.media_stream_mic": 1,  # Microphone
    "profile.default_content_setting_values.notifications": 2  # Desktop Notifications
}
options.add_experimental_option("prefs", prefs)
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=service, options=options)

location_test_website = "https://whatmylocation.com/"
camera_test_website = "https://webcamtests.com/"
microphone_test_website = "https://mictests.com/"
desktop_notif_test_website = "https://web-push-book.gauntface.com/demos/notification-examples/"

driver.get("https://www.play1.automationcamp.ir/index.html")
driver.execute_script("Notification.requestPermission()")
sleep(10)