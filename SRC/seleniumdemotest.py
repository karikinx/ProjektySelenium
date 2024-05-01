from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import random

user_login = str(random.randint(1, 10000)) + "karikinx@gmail.com"
password = "#1QAZwsx#1"
wrong_password = "#1QAZwsx#111"
def test_register_passed():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://seleniumdemo.com/?page_id=7")
    driver.find_element(By.ID, "reg_email").click()
    driver.find_element(By.ID, "reg_email").send_keys(user_login)
    driver.find_element(By.ID, "reg_password").click()
    driver.find_element(By.ID, "reg_password").send_keys(password)
    driver.find_element(By.NAME, "register").click()
    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()
    time.sleep(3)


def test_log_in_passed():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://seleniumdemo.com/?page_id=7")
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys(user_login)
    driver.find_element(By.ID, "password").click()
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.NAME, "login").click()
    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()
    time.sleep(3)


def test_log_in_failed():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://seleniumdemo.com/?page_id=7")
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys(user_login)
    driver.find_element(By.ID, "password").click()
    driver.find_element(By.ID, "password").send_keys(wrong_password)
    driver.find_element(By.NAME, "login").click()
    assert ": Incorrect username or password." in driver.find_element(By.XPATH, "//ul[@class='woocommerce-error']//li").text
    time.sleep(3)