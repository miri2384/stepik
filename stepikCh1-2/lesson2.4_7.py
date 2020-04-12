from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
   browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
   browser.implicitly_wait(1)
   browser.get(link)

   price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
   #button = browser.find_element_by_id("price")
   button = browser.find_element_by_css_selector("button.btn") 
   button.click()

   x_element = browser.find_element_by_id("input_value")
   x = x_element.text
   y = calc(x)
   input0 = browser.find_element_by_id("answer")
   input0.send_keys(y)
	
   button1 = browser.find_element_by_id("solve") 
   button1.click()
   
   
finally:
   time.sleep(5)
   browser.quit()
