from selenium import webdriver
import time
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import random

def test_address_change():
    driver = driver_setup(WEBSITE_LINK)
