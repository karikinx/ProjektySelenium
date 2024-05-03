from selenium import webdriver
import time
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import random

CORRECT_PASSWORD = "#1QAZwsx#1"
WRONG_PASSWORD = "#1QAZwsx#111"


def generate_login():
    return str(random.randint(1, 5)) + "karikinx@gmail.com"


def driver_setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://seleniumdemo.com/?page_id=7")
    return driver


def fill_in_registration_form(driver, login, password):
    driver.find_element(By.ID, "reg_email").click()
    driver.find_element(By.ID, "reg_email").clear()
    driver.find_element(By.ID, "reg_email").send_keys(login)

    driver.find_element(By.ID, "reg_password").click()
    driver.find_element(By.ID, "reg_password").clear()
    driver.find_element(By.ID, "reg_password").send_keys(password)


def test_register_passed():
    driver = driver_setup()
    user_login = generate_login()
    fill_in_registration_form(driver, user_login, CORRECT_PASSWORD)
    driver.find_element(By.NAME, "register").click()
    time.sleep(5)
    try:
        while ("An account is already registered with your email address. Please log in."
               in driver.find_element(By.XPATH, "//ul[@class='woocommerce-error']//li")
                       .text):
            print("Error message found")
            driver.close()

            driver = driver_setup()
            user_login = generate_login()
            fill_in_registration_form(driver, user_login, CORRECT_PASSWORD)
            driver.find_element(By.NAME, "register").click()
            time.sleep(5)
    except NoSuchElementException as e:
        print("Error message not found")
        assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()
        time.sleep(5)


# def test_log_in_passed():
#     driver = test_setup()
#     driver.find_element(By.ID, "username").click()
#     driver.find_element(By.ID, "username").send_keys(user_login)
#     driver.find_element(By.ID, "password").click()
#     driver.find_element(By.ID, "password").send_keys(password)
#     driver.find_element(By.NAME, "login").click()
#     assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()
#     time.sleep(3)
#
#
# def test_log_in_failed():
#     driver = test_setup()
#     driver.find_element(By.ID, "username").click()
#     driver.find_element(By.ID, "username").send_keys(user_login)
#     driver.find_element(By.ID, "password").click()
#     driver.find_element(By.ID, "password").send_keys(wrong_password)
#     driver.find_element(By.NAME, "login").click()
#     assert ": Incorrect username or password." in driver.find_element(By.XPATH, "//ul[@class='woocommerce-error']//li").text
#     time.sleep(3)
