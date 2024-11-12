from selenium.webdriver.common.by import By  
import pytest
import conftest
from pages.login_page import LoginPage
from pages.catalog_page import CatalogPage

@pytest.mark.usefixtures("setup_teardown")
def test_CT07_padrao_catalogo():
    driver = conftest.driver 
    login_page = LoginPage()
    catalog_page = CatalogPage()
    
    login_page.fazer_login("standard_user", "secret_sauce")
    assert driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div').is_displayed()