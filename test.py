import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome() 

driver.get("dev.invest-ra.ru")
driver.find_element_by_id("mat-button-focus-overlay").click()
time.sleep(1)
driver.find_element_by_id("email").click()
driver.find_element_by_id("email").send_keys("stuffy.user.0101@gmail.com")
time.sleep(1)
driver.find_element_by_name("pass").clear()
driver.find_element_by_name("pass").send_keys("TUnke3RW4gm4YM8")
time.sleep(1)
driver.find_element_by_id("btn-entrance").click()
driver.find_element_by_css_selector("/html/body/app-root/div/app-navbar/mat-toolbar/div/div/a[4]").click()
time.sleep(1)
driver.find_element_by_id("mat-card mat-focus-indicator credit").click()
time.sleep(1)
driver.find_element_by_id("mat-form-field-infix ng-tns-c84-521").click()
driver.find_element_by_id("credit").clear()
driver.find_element_by_id("credit").send_keys("10000")
time.sleep(1)
driver.find_element_by_id("mat-content ng-tns-c152-809").click()
time.sleep(3)

driver.close()