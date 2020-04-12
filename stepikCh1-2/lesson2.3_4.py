from selenium import  webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    submit = browser.find_element_by_css_selector("button.btn") 
    submit.click()
	
    confirm = browser.switch_to.alert
    confirm.accept()
	
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input0 = browser.find_element_by_id("answer")
    input0.send_keys(y)
	
    button = browser.find_element_by_css_selector("button.btn") 
    button.click()
	
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()  
	
    