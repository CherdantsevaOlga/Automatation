from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))


driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/entry_ad")
sleep(2)

driver.find_element(By.XPATH, "//div[@class='modal-footer']").click()
sleep(5)