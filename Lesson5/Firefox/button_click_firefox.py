from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()


driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/add_remove_elements/')


for i in range(5):
    button = driver.find_element(By.XPATH, "//button[@onclick='addElement()']")
    button.click()


delete_buttons = driver.find_elements(By.XPATH, ("//button[text()='Delete']"))


print(f"Количество кнопок 'Delete': {len(delete_buttons)}")


sleep(10)
driver.quit()