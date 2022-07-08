from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from threading import Thread
import time

# This array 'caps' defines the capabilities browser, device and OS combinations where the test will run
caps=[{
      'device': 'Samsung Galaxy S20',
      'os_browser': '11.0',
      'real_mobile': 'true',
      'name': 'Parallel Test1',
      'build': 'BStackDemo Cart Test Python'
      },
      {
      'device': 'iPhone 13 Mini',
      'os_browser': '14',
      'real_mobile': 'true',
      'name': 'Parallel Test2',
      'build': 'BStackDemo Cart Test Python'
}]

#run_session function adds a product in cart bstackdemo.com
def run_session(desired_cap):
  driver = webdriver.Remote(
      command_executor=' ',
      desired_capabilities=desired_cap)
  try:
    driver.get("https://bstackdemo.com/")

    time.sleep(1)

    item1_on_page = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id=\"1\"]/p'))).text
    #driver.find_element_by_xpath("//*[@id=\"1\"]/p").text
    

    item2_on_page = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id=\"8\"]/p'))).text
    #driver.find_element_by_xpath("//*[@id=\"8\"]/p").text
    

    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id=\"1\"]/div[4]'))).click()
    
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id=\"__next\"]/div/div/div[2]/div[1]'))).click()
   
   WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id=\"8\"]/div[4]'))).click()
   #driver.find_element_by_xpath("//*[@id=\"1\"]/div[4]").click()
    
    # //*[@id="__next"]/div/div/div[2]/div[1]

    #driver.find_element_by_xpath("//*[@id=\"__next\"]/div/div/div[2]/div[1]").click()
    
    #driver.find_element_by_xpath("//*[@id=\"8\"]/div[4]").click()

    ## Get text of product in cart //*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div[1]/div[3]/p[1]
    item1_in_cart = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id=\"__next\"]/div/div/div[2]/div[2]/div[2]/div/div[3]/p[1]'))).text
    #driver.find_element_by_xpath("//*[@id=\"__next\"]/div/div/div[2]/div[2]/div[2]/div/div[3]/p[1]").text
    item2_in_cart = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id=\"__next\"]/div/div/div[2]/div[2]/div[2]/div[2]/div[3]/p[1]'))).text
    #driver.find_element_by_xpath("//*[@id=\"__next\"]/div/div/div[2]/div[2]/div[2]/div[2]/div[3]/p[1]").text

    time.sleep(1)
    # Verify whether the product (iPhone 12) is added to cart
    if item1_on_page == item1_in_cart and item2_on_page == item2_in_cart:
        # Set the status of test as 'passed' or 'failed' based on the condition; if item is added to cart
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "iPhone 12 and XR have been successfully added to the cart!"}}')

  except NoSuchElementException:
      driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some elements failed to load"}}')

  # Stop the driver
  driver.quit()

#The Thread function takes run_session function and each set of capability from the caps array as an argument to run each session in parallel
for cap in caps:
  Thread(target=run_session, args=(cap,)).start()
