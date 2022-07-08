from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from threading import Thread
import time


# This array 'caps' defines the capabilities browser, device and OS combinations where the test will run
caps=[{
      'device': 'Samsung Galaxy S20',
      'os_browser': '11.0',
      'real_mobile': 'true',
      'name': 'Parallel Test1',
      'build': 'BStackDemo Login Test Python'
      },
      {
      'device': 'iPhone 13 Mini',
      'os_browser': '14',
      'real_mobile': 'true',
      'name': 'Parallel Test2',
      'build': 'BStackDemo Login Test Python'
}]

#run_session function adds a product in cart bstackdemo.com
def run_session(desired_cap):
  driver = webdriver.Remote(
      command_executor='https://parthdode_aWxDeC:7LcszpsTsuSLppLhhquA@hub-cloud.browserstack.com/wd/hub',
      desired_capabilities=desired_cap)
  try:
    driver.get("https://bstackdemo.com/signin")
    ####
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id=\"username\"]/div/div[2]/span'))).click()
    
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id=\"username\"]/div[2]/div'))).click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id=\"password\"]/div/div[2]/span'))).click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id=\"password\"]/div[2]/div'))).click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'login-btn'))).click()
    ####
    #driver.find_element_by_xpath("//*[@id=\"username\"]/div/div[2]/span").click()
    #time.sleep(5)
    #driver.find_element_by_xpath("//*[@id=\"username\"]/div[2]/div").click()

    #time.sleep(5)

    #driver.find_element_by_xpath("//*[@id=\"password\"]/div/div[2]/span").click()
    #time.sleep(5)

    #driver.find_element_by_xpath("//*[@id=\"password\"]/div[2]/div").click()
    #time.sleep(5)
    #driver.find_element_by_id("login-btn").click()

    #username_input_box.send_keys(username)
    #time.sleep(2)
    #password_input_box.send_keys(password)

    #time.sleep(2)

    #hit the login button

    # automatically close the driver after 30 seconds
    time.sleep(30)
    # Set the status of test as 'passed' or 'failed' based on the condition; if item is added to cart
    driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Login Succeded!"}}')

  except NoSuchElementException:
      driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Login Failed!"}}')

  # Stop the driver
  driver.quit()

#The Thread function takes run_session function and each set of capability from the caps array as an argument to run each session in parallel
for cap in caps:
  Thread(target=run_session, args=(cap,)).start()
