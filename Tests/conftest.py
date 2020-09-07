import time

import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def setup(request):
    driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    time.sleep(4)
    driver.maximize_window()
    request.cls.driver = driver

    #yield
    #driver.close()
