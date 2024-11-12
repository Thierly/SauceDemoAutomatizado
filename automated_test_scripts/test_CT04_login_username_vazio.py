import pytest
from selenium.webdriver.common.by import By  
import conftest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
def test_CT04_login_username_vazio():
    driver = conftest.driver 
    login_page = LoginPage()
    
    login_page.fazer_login("", "secret_sauce")
    assert driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3').is_displayed()