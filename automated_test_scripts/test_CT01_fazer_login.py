from selenium.webdriver.common.by import By  
import pytest
import conftest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
def test_CT01_fazer_login_com_sucesso():
    driver = conftest.driver 
    login_page = LoginPage()
    
    login_page.fazer_login("standard_user", "secret_sauce")
 
    assert driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/span").is_displayed()
