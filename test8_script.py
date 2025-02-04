


from selenium import webdriver
from selenium.webdriver.common.by import By
import time





try:

    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    
    x_element = browser.find_element(By.ID, "num1")
    y_element = browser.find_element(By.ID, "num2")
    x = x_element.text
    y = y_element.text
    y1 = str(int(x)+int(y))

    selector = f'option[value="{y1}"]'
    print(y1)
    print(x)
    print(y)
   

    option1 = browser.find_element(By.ID, "dropdown").click()
    option2 = browser.find_element(By.CSS_SELECTOR, selector).click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()



finally:
    
    time.sleep(10)
    browser.quit()
