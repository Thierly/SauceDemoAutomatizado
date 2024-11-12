import pytest
from selenium import webdriver

driver: webdriver.Remote


@pytest.fixture
def setup_teardown():

    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(1)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    yield

    driver.quit()