from selenium.webdriver.common.by import By  
import pytest
import conftest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
def test_CT06_logout():
    driver = conftest.driver 
    login_page = LoginPage()
    
    login_page.fazer_login("standard_user", "secret_sauce")
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    driver.find_element(By.ID, "logout_sidebar_link").click()
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]').is_displayed()