from selenium.webdriver.common.by import By  
import pytest
import conftest
from pages.login_page import LoginPage
from pages.catalog_page import CatalogPage
from pages.cart_page import CartPage
from pages.base_page import BasePage

@pytest.mark.usefixtures("setup_teardown")
def test_CT21_produto_persiste_ao_carrinho_ao_voltar_ao_catalogo():
    driver = conftest.driver 
    login_page = LoginPage()
    catalog_page = CatalogPage()
    cart_page = CartPage()
    base_page = BasePage()
    
    login_page.fazer_login("standard_user", "secret_sauce")
    catalog_page.abrir_descrição_do_produto
    cart_page.adicionar_produto()
    catalog_page.voltar_ao_catalogo()
    cart_page.abrir_carrinho()

    
    assert driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').is_displayed()