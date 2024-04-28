from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import random

def test_log_in_passed():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://seleniumdemo.com/?page_id=7")
    driver.find_element(By.ID, "reg_email").click()
    email = str(random.randint(1, 10000)) + "karikinx@gmail.com"
    password = "#1QAZwsx#1"
    driver.find_element(By.ID, "reg_email").send_keys(email)
    driver.find_element(By.ID, "reg_password").click()
    driver.find_element(By.ID, "reg_password").send_keys(password)
    driver.find_element(By.NAME, "register").click()
    time.sleep(3)
    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()
