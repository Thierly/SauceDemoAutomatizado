import pytest
from selenium.webdriver.common.by import By  
import conftest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
def test_CT02_login_invalido():
    driver = conftest.driver 
    login_page = LoginPage()
    
    login_page.fazer_login("error_test", "1234")
    assert driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3').is_displayed()
    