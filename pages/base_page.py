import conftest

class BasePage:
    def __init__(self) -> None:
        self.driver = conftest.driver
    
    def encontrar_elemento(self, locator):
        return self.driver.find_element(*locator)
    
    def encontrar_elementos(self, locator):
        return self.driver.find_elements(*locator)
    
    def escrever(self, locator, text): 
        self.encontrar_elemento(locator).send_keys(text)
    
    def clicar(self, locator):
        self.encontrar_elemento(locator).click()
    
    
