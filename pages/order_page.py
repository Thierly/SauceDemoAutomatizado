import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderPage(BasePage):
    def __init__(self) -> None:
     self.driver = conftest.driver
     self.base_page = BasePage()
     self.first_name_field = (By.ID, "first-name")
     self.last_name_field = (By.ID, "last-name")
     self.postal_code_field = (By.ID, "postal-code")
     self.continue_btn = (By.ID, "continue")
     self.cancel_btn = (By.ID, "cancel")
     self.finish_btn = (By.ID, "finish")

    def fazer_pedido(self, firstname, lastname, zipcode):
       self.base_page.escrever(self.first_name_field, firstname)
       self.base_page.escrever(self.last_name_field, lastname)
       self.base_page.escrever(self.postal_code_field, zipcode)
       self.base_page.clicar(self.continue_btn)
       self.base_page.clicar(self.finish_btn)
    
    def cancelar_pedido(self):
       self.base_page.clicar(self.cancel_btn)
    
    def cancelar_pedido_pos_checkout(self, firstname, lastname, zipcode):
       self.base_page.escrever(self.first_name_field, firstname)
       self.base_page.escrever(self.last_name_field, lastname)
       self.base_page.escrever(self.postal_code_field, zipcode)
       self.base_page.clicar(self.cancel_btn)
    
       
       
       