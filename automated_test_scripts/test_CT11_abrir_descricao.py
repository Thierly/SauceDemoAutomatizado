from selenium.webdriver.common.by import By  
import pytest
import conftest
from pages.login_page import LoginPage
from pages.catalog_page import CatalogPage

@pytest.mark.usefixtures("setup_teardown")
def test_CT11_abrir_descriçao():
    driver = conftest.driver 
    login_page = LoginPage()
    catalog_page = CatalogPage()
    
    login_page.fazer_login("standard_user", "secret_sauce")
    catalog_page.abrir_descrição_do_produto()
    assert driver.find_element(By.XPATH, '//*[@id="back-to-products"]').is_displayed()