import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self) -> None:
        self.driver = conftest.driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.menu = (By.ID, "react-burger-menu-btn")
        self.logout = (By.ID, "logout_sidebar_link")
    
    def fazer_login(self, usuario, senha):
        self.driver.find_element(*self.username_field).send_keys(usuario)
        self.driver.find_element(*self.password_field).send_keys(senha)
        self.driver.find_element(*self.login_button).click()
    
    def fazer_logout(self):
        self.driver.find_element(*self.menu).click()
        self.driver.find_element(*self.logout).click()
        
        
