from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/execute_script.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
   browser = webdriver.Chrome()
   browser.get(link)
   x_element = browser.find_element_by_id("input_value")
   x = x_element.text
   y = calc(x)
   input2 = browser.find_element_by_id("robotsRule")
   browser.execute_script("return arguments[0].scrollIntoView(true);", input2)
   input0 = browser.find_element_by_id("answer")
   input0.send_keys(y)
   browser.execute_script("window.scrollBy(0, 120);")
   input1 = browser.find_element_by_id("robotCheckbox")
   input1.click()
   input2 = browser.find_element_by_id("robotsRule")
   input2.click()
 
      
   button = browser.find_element_by_css_selector("button.btn")
   button.click()

finally:
   # успеваем скопировать код за 30 секунд
   time.sleep(10)
   # закрываем браузер после всех манипуляций
   browser.quit()
   
   #empty string