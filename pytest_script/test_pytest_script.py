"""
-s (or --capture=no): This option disables the output capturing. 
                      By default, pytest captures the output of your tests and only displays it if the test fails. 
                      Using -s disables this capturing, allowing you to see the output even for passing tests.

-v (or --verbose): This option increases the verbosity of the output. 
                   By default, pytest provides concise output, showing only the names of the test modules and the results. 
                   Adding -v increases the verbosity, providing more detailed information 


1]To run particular testcase cmd : pytest -sv test_pytest_script.py::test_blank_usernm_pwd
2]to generate html report : $ pip3 install pytest-html
                            pytest -sv test_pytest_script.py --html=<report name>.html
3]to run grouped testcases : pytest -sv test_pytest_script.py -m <grouped testcase nm>

fixtures:
1]skip testcase: @pytest.mark.skip(reason="no way of currently testing this")
2]skip testcase if a condition is true: @pytest.mark.skipif(sys.platform == "win32", reason="does not run on windows")
3]fail a testcase explicitly : @pytest.mark.xfail(sys.platform == "win32", reason="bug in a 3rd party library")
                               @pytest.mark.xfail(raises=RuntimeError)
                               @pytest.mark.xfail(reason="known parser issue")
                            
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import pytest_html

def setup_module():
    global driver,wait30,wait120
    chrome_options=webdriver.ChromeOptions()
    driver=webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    wait30=WebDriverWait(driver,30)
    wait120=WebDriverWait(driver,120)
    url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver.get(url)

@pytest.mark.blank
def test_blank_usernm_pwd():
    wait30.until(EC.element_to_be_clickable((By.XPATH,'//button[@type="submit"]'))).click()
    try:
        get_required_msg_username=wait30.until(EC.presence_of_element_located((By.XPATH,'//span[@class="oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message" and contains(text(),Required)]/../div/input[@name="username"]')))
        get_required_msg_pwd=wait30.until(EC.presence_of_element_located((By.XPATH,'//span[@class="oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message" and contains(text(),Required)]/../div/input[@name="password"]')))
        if get_required_msg_username and get_required_msg_pwd:
            assert True
        else:
            assert False, "Issue"
    except:
        assert False, "Error doesnt show required msg on blank"

    driver.refresh()

@pytest.mark.blank
def test_blank_username():
    pwd_txtbox=wait30.until(EC.presence_of_element_located((By.NAME,"password")))
    pwd_txtbox.send_keys("admin@123")
    wait30.until(EC.element_to_be_clickable((By.XPATH,'//button[@type="submit"]'))).click()
    try:
        get_required_msg_username=wait30.until(EC.presence_of_element_located((By.XPATH,'//span[@class="oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message" and contains(text(),Required)]/../div/input[@name="username"]')))
        
        if get_required_msg_username:
            assert True
        else:
            assert False, "Issue"
    except:
        assert False, "Error doesnt show required msg on blank"
    
    driver.refresh()

@pytest.mark.blank
def test_blank_pwd():
    username_txtbox=wait30.until(EC.presence_of_element_located((By.NAME,"username")))
    username_txtbox.send_keys("Admin")
    wait30.until(EC.element_to_be_clickable((By.XPATH,'//button[@type="submit"]'))).click()
    try:
        get_required_msg_pwd=wait120.until(EC.presence_of_element_located((By.XPATH,'//span[@class="oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message" and contains(text(),Required)]/../div/input[@name="password"]')))
        
        if get_required_msg_pwd:
            assert True
        else:
            assert False, "Issue"
    except:
        assert False, "Error doesnt show required msg on blank"
    driver.refresh()

@pytest.mark.logincred
def test_incorrect_username_pwd():
    username_txtbox=wait30.until(EC.presence_of_element_located((By.NAME,"username")))
    username_txtbox.send_keys("admin0")
    pwd_txtbox=wait30.until(EC.presence_of_element_located((By.NAME,"password")))
    pwd_txtbox.send_keys("admin@123")
    wait30.until(EC.element_to_be_clickable((By.XPATH,'//button[@type="submit"]'))).click()
    try:
        get_error_msg=wait30.until(EC.presence_of_element_located((By.XPATH,'//p[@class="oxd-text oxd-text--p oxd-alert-content-text"]'))).get_attribute("innerHTML")
        if get_error_msg in ["Invalid credentials","Incorrect username or password"]:
            assert True
        else:
            assert False, "Issue"
    except:
        assert False, "Error element missing"

    wait30.until(EC.presence_of_element_located((By.NAME,"username"))).clear()
    wait30.until(EC.presence_of_element_located((By.NAME,"password"))).clear()

@pytest.mark.logincred
def test_incorrect_username_crt_pwd():
    username_txtbox=wait30.until(EC.presence_of_element_located((By.NAME,"username")))
    username_txtbox.send_keys("admin0")
    pwd_txtbox=wait30.until(EC.presence_of_element_located((By.NAME,"password")))
    pwd_txtbox.send_keys("admin123")
    wait30.until(EC.element_to_be_clickable((By.XPATH,'//button[@type="submit"]'))).click()
    try:
        get_error_msg=wait30.until(EC.presence_of_element_located((By.XPATH,'//p[@class="oxd-text oxd-text--p oxd-alert-content-text"]'))).get_attribute("innerHTML")
        if get_error_msg in ["Invalid credentials","Incorrect username or password"]:
            assert True
        else:
            assert False, "Issue"
    except:
        assert False, "Error element missing"

    wait30.until(EC.presence_of_element_located((By.NAME,"username"))).clear()
    wait30.until(EC.presence_of_element_located((By.NAME,"password"))).clear()

@pytest.mark.logincred
def test_crt_usernm_incorrect_pwd():
    username_txtbox=wait30.until(EC.presence_of_element_located((By.NAME,"username")))
    username_txtbox.send_keys("Admin")
    pwd_txtbox=wait30.until(EC.presence_of_element_located((By.NAME,"password")))
    pwd_txtbox.send_keys("admin@123")
    wait30.until(EC.element_to_be_clickable((By.XPATH,'//button[@type="submit"]'))).click()
    try:
        get_error_msg=wait30.until(EC.presence_of_element_located((By.XPATH,'//p[@class="oxd-text oxd-text--p oxd-alert-content-text"]'))).get_attribute("innerHTML")
        if get_error_msg in ["Invalid credentials","Incorrect username or password"]:
            assert True
        else:
            assert False, "Issue"
    except:
        assert False, "Error element missing"

    wait30.until(EC.presence_of_element_located((By.NAME,"username"))).clear()
    wait30.until(EC.presence_of_element_located((By.NAME,"password"))).clear()

@pytest.mark.logincred
def test_incorrect_usernm_pwd():
    username_txtbox=wait30.until(EC.presence_of_element_located((By.NAME,"username")))
    username_txtbox.send_keys("admin0")
    pwd_txtbox=wait30.until(EC.presence_of_element_located((By.NAME,"password")))
    pwd_txtbox.send_keys("admin123")
    wait30.until(EC.element_to_be_clickable((By.XPATH,'//button[@type="submit"]'))).click()
    try:
        get_error_msg=wait30.until(EC.presence_of_element_located((By.XPATH,'//p[@class="oxd-text oxd-text--p oxd-alert-content-text"]'))).get_attribute("innerHTML")
        if get_error_msg in ["Invalid credentials","Incorrect username or password"]:
            assert True
        else:
            assert False, "Issue"
    except:
        assert False, "Error element missing"

    wait30.until(EC.presence_of_element_located((By.NAME,"username"))).clear()
    wait30.until(EC.presence_of_element_located((By.NAME,"password"))).clear()

@pytest.mark.login
def test_correct_username_pwd():
    wait30.until(EC.presence_of_element_located((By.NAME,"username"))).send_keys("Admin")
    wait30.until(EC.presence_of_element_located((By.NAME,"password"))).send_keys("admin123")
    wait30.until(EC.element_to_be_clickable((By.XPATH,'//button[@type="submit"]'))).click()
    try:
        get_error_msg=wait30.until(EC.presence_of_element_located((By.XPATH,'//p[@class="oxd-text oxd-text--p oxd-alert-content-text"]'))).get_attribute("innerHTML")
        if get_error_msg in ["Invalid credentials","Incorrect username or password"]:
            assert False, "Issue, as for correct credentials login denied"
        else:
            assert True
    except:
        assert True

    get_current_url=driver.current_url
    print("current-url",get_current_url)
    get_title=driver.title
    print("current-title",get_title)
    expected_current_url="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    if expected_current_url==get_current_url:
        assert True
    else:
        assert False,"route login issue"

    try:
        wait30.until(EC.presence_of_element_located((By.XPATH,'//h6[@class="oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module" and contains(text(),Dashboard)]')))
        assert True
    except:
        assert False, "Login issue"


def teardown_module():
    driver.quit()