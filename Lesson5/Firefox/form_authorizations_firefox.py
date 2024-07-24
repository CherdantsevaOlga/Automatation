from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()


driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/login")

username_input = driver.find_element(By.XPATH, "//input[@id='username']")
username_input.send_keys("tomsmith")
password_input = driver.find_element(By.XPATH, "//input[@id='password']")
password_input.send_keys("SuperSecretPassword!")
login_click = driver.find_element(By.XPATH, "//button[@type='submit']").click()

sleep(5)
driver.quit()