from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/entry_ad")
sleep(2)
driver.find_element(By.XPATH, "//div[@class='modal-footer']").click()

sleep(5)
driver.quit()