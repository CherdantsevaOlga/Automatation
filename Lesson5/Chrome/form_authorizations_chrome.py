from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))


driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/login")

username_input = driver.find_element(By.XPATH, "//input[@id='username']")
username_input.send_keys("tomsmith")
password_input = driver.find_element(By.XPATH, "//input[@id='password']")
password_input.send_keys("SuperSecretPassword!")
login_click = driver.find_element(By.XPATH, "//button[@type='submit']").click()


sleep(5)