from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

chrome_options=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=chrome_options)
wait30=WebDriverWait(driver,30)

url = "https://practicetestautomation.com/practice-test-login/"
driver.get(url)

get_usernm_path=wait30.until(EC.presence_of_element_located((By.ID,"username"))).send_keys("student")
get_pwd_path=wait30.until(EC.presence_of_element_located((By.ID,"password"))).send_keys("Password123")

click_submit=wait30.until(EC.element_to_be_clickable((By.ID,"submit"))).click()

try:
    login_success=wait30.until(EC.presence_of_element_located((By.CLASS_NAME,"post-title")))
    driver.get_screenshot_as_file("success.png")
    #driver.save_screenshot("success.png") -- Gets the screenshot of the current window.
    #driver.get_screenshot_as_png() --Gets the screenshot of the current window as a binary data string format.
    #print(driver.get_screenshot_as_base64())  -- ASCII Representation of binary data as string format
    print("loggedin success")
except:
    driver.get_screenshot_as_file("failure.png")
    print("login unsuccessfull")

print("done")
    


