from selenium import webdriver
import time
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import random
WEBSITE_LINK = "http://seleniumdemo.com/?page_id=7"
CORRECT_PASSWORD = "#1QAZwsx#1"
WRONG_PASSWORD = "#1QAZwsx#111"
CORRECT_LOGIN = ""


def generate_login():
    return str(random.randint(1, 2000)) + "karikinx@gmail.com"


def driver_setup(link):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(link)
    return driver


def fill_in_registration_form(driver, login, password):
    driver.find_element(By.ID, "reg_email").click()
    driver.find_element(By.ID, "reg_email").send_keys(login)
    driver.find_element(By.ID, "reg_password").click()
    driver.find_element(By.ID, "reg_password").send_keys(password)

def fill_in_login_form(driver, login, password):
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys(login)
    driver.find_element(By.ID, "password").click()
    driver.find_element(By.ID, "password").send_keys(password)

def test_register_passed():
    driver = driver_setup(WEBSITE_LINK)
    user_login = generate_login()
    fill_in_registration_form(driver, user_login, CORRECT_PASSWORD)
    driver.find_element(By.NAME, "register").click()
    time.sleep(1)
    try:
        while ("An account is already registered with your email address. Please log in."
               in driver.find_element(By.XPATH, "//ul[@class='woocommerce-error']//li")
                       .text):
            driver.close()

            driver = driver_setup(WEBSITE_LINK)
            user_login = generate_login()
            fill_in_registration_form(driver, user_login, CORRECT_PASSWORD)
            driver.find_element(By.NAME, "register").click()
    except NoSuchElementException as e:
        assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()
    global CORRECT_LOGIN
    CORRECT_LOGIN = user_login
def test_log_in_passed():
    driver = driver_setup(WEBSITE_LINK)
    fill_in_login_form(driver, CORRECT_LOGIN, CORRECT_PASSWORD)
    driver.find_element(By.NAME, "login").click()
    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()

def test_log_in_failed():
    driver = driver_setup(WEBSITE_LINK)
    fill_in_login_form(driver, CORRECT_LOGIN, WRONG_PASSWORD)
    driver.find_element(By.NAME, "login").click()
    assert ": Incorrect username or password." in driver.find_element(By.XPATH, "//ul[@class='woocommerce-error']//li").text
