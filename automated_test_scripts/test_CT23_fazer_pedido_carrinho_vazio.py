from selenium.webdriver.common.by import By  
import pytest
import conftest
from pages.login_page import LoginPage
from pages.catalog_page import CatalogPage
from pages.cart_page import CartPage
from pages.base_page import BasePage
from pages.order_page import OrderPage

@pytest.mark.usefixtures("setup_teardown")
def test_CT23_fazer_pedido_com_carrinho_vazio():
    driver = conftest.driver 
    login_page = LoginPage()
    catalog_page = CatalogPage()
    cart_page = CartPage()
    base_page = BasePage()
    order_page = OrderPage()

    login_page.fazer_login("standard_user", "secret_sauce")
    cart_page.abrir_carrinho()
    cart_page.checkout()
    order_page.fazer_pedido("Juca", "Tatu", "00002")

    assert not driver.find_element(By.XPATH, '//*[@id="checkout_complete_container"]/img').is_displayed()
