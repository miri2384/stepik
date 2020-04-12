from selenium import webdriver
import time
import math

link= "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
   browser = webdriver.Chrome()
   browser.get(link)
   submit = browser.find_element_by_css_selector("button.trollface ")
   submit.click()
   new_window = browser.window_handles[1]
   browser.switch_to_window(new_window)
   x_element = browser.find_element_by_id("input_value")
   x = x_element.text
   y = calc(x)
   input0 = browser.find_element_by_id("answer")
   input0.send_keys(y)
	
   button = browser.find_element_by_css_selector("button.btn") 
   button.click()
	
finally:
   time.sleep(10)
   browser.quit()

   
