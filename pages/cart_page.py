import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self):
     self.driver = conftest.driver
     self.adicionar_mochila = (By.ID, "add-to-cart-sauce-labs-backpack")
     self.remover_mochila = (By.ID, "remove-sauce-labs-backpack")
     self.adicionar_camisa = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
     self.carrinho = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
     self.botao_checkout = (By.ID, "checkout")



    def adicionar_produto(self):
       self.clicar(self.adicionar_mochila)
    
    def remover_produto(self):
       self.clicar(self.remover_mochila)
    
    def adicionar_camiseta(self):
       self.clicar(self.adicionar_camisa)
    
    def abrir_carrinho(self):
       self.clicar(self.carrinho)
    
    def checkout(self):
       self.clicar(self.botao_checkout)
       
       
