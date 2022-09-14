from lib2to3.pgen2 import driver
from re import search
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
url ="https://github.com"
driver.get(url)

# searchInput = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div/div/div[1]/div/div/form/label/input[1]") alternatif yol
searchInput = driver.find_element_by_name("q")
time.sleep(1)
searchInput.send_keys("python") #anahtar kelime
time.sleep(1)
searchInput.send_keys(Keys.ENTER)
time.sleep(1)
result = driver.find_elements_by_css_selector(".repo-list-item .text-normal a")

for element in result:
    print(element.text)

driver.close()