from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import json
from selenium.webdriver.common.by import By
from time import sleep

user_dir = "C:/Users/MM/Documents/AutomationCamp/temp/user_dir"
options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={user_dir}")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(3)


# 1- Check Requests and Responses

def get_all_requests_of_session():
    return driver.requests


def get_specific_request_of_session(url, property_return, all_requests=None):
    """
    Return a request to the 'url'
    :param all_requests: Previously caught requests
    :param url: Url of that specific request
    :param property_return: Use one of these: ['object', 'body', 'headers', 'response_body', 'host', 'path', 'url, 'date', 'ws']
    :return: Intercepted request
    """
    property_return = property_return.lower()

    if all_requests is None:
        driver.wait_for_request(pat=url)
        all_requests = get_all_requests_of_session()
    for request in all_requests:
        if url in request.url:
            if property_return == 'object':
                return request
            if property_return == 'body':
                return json.loads(request.body)
            elif property_return == 'headers':
                return request.headers
            elif property_return == 'response_body':
                return json.loads(request.response.body)
            elif property_return == 'host':
                return request.host
            elif property_return == 'path':
                return request.path
            elif property_return == 'url':
                return request.url
            elif property_return == 'date':
                return request.host
            elif property_return == 'ws':
                return request.ws_messages
            else:
                raise Exception(f" 'property_return' argument is not supported")

driver.get("http://localhost:8020/signup")
driver.find_element(By.ID, "firstName").send_keys("Mohammad")
driver.find_element(By.ID, "lastName").send_keys("Monfared")
driver.find_element(By.ID, "username").send_keys("automationcamp2")
driver.find_element(By.ID, "password").send_keys("Abcde@123")
driver.find_element(By.ID, "confirmPassword").send_keys("Abcde@123")
driver.find_element(By.XPATH, "//button[@data-test='signup-submit']").click()
sleep(2)

signup_request = get_specific_request_of_session(url="/users", property_return="response_body")
print(signup_request)
print(type(signup_request))
assert signup_request['user']['firstName'] == "Mohammad"
assert signup_request['user']['lastName'] == "Monfared"
assert signup_request['user']['username'] == "automationcamp2"

# 2- Wait for request

driver.get("http://localhost:8020/signin")
driver.find_element(By.ID, 'username').send_keys("automationcamp2")
driver.find_element(By.ID, 'password').send_keys("Abcde@123")
driver.find_element(By.XPATH, "//*[@data-test='signin-submit']").click()
sleep(1)
driver.wait_for_request(pat="/login")

# 3 Interceptor > Block Request

def block_svg(request):
    if ".svg" in request.url:
        request.abort()

driver.request_interceptor = block_svg
driver.get("http://localhost:8020/signin")
sleep(2)
driver.find_element(By.ID, 'username').send_keys("automationcamp2")
driver.find_element(By.ID, 'password').send_keys("Abcde@123")
driver.find_element(By.XPATH, "//*[@data-test='signin-submit']").click()
sleep(1)

# 4 Interceptor > Update JSON in a POST request body

def change_request(request):
    if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
        body = request.body.decode('utf-8')     # to string
        data = json.loads(body)     # string to json
        data['username'] = 'automationcamp2'       # update json
        request.body = json.dumps(data).encode('utf-8')   # set the JSON back to the request
        # fix body length
        del request.headers['Content-Length']
        request.headers['Content-Length'] = str(len(request.body))

driver.request_interceptor = change_request
driver.get("http://localhost:8020/signin")
sleep(2)
driver.find_element(By.ID, 'username').send_keys("nebgioKEGdkgjkjl")
driver.find_element(By.ID, 'password').send_keys("Abcde@123")
driver.find_element(By.XPATH, "//*[@data-test='signin-submit']").click()
sleep(1)

# 5 Interceptor > Mock a response

def mock_response(request):
    if 'favicon.ico' in request.url:
        request.create_response(
            status_code=201,
            # headers={"Content-Type" : "application/json"},
            # body = json.dumps({"tx_id": "a125412f14844521b656", "ref_id": 154}).encode('utf-8')
            headers={"Content-Type": "text/html"},
            body="<html><h2> Response Mocked </h2></html>"
        )
driver.request_interceptor = mock_response
sleep(2)
driver.get("https://www.play2.automationcamp.ir/index.html")
sleep(5)

# 6 Unset an Interceptor

del driver.request_interceptor
driver.refresh()
sleep(3)