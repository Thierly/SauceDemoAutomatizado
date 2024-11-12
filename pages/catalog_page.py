import conftest
from selenium.webdriver.common.by import By

class CatalogPage:
    def __init__(self) -> None:
        self.driver = conftest.driver
        self.catalog_filter = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select')
        self.name_z_to_a = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[2]')
        self.price_high_to_low = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[4]')
        self.price_low_to_high = (By.XPATH,'//*[@id="header_container"]/div[2]/div/span/select/option[3]')
        self.mochila = (By.XPATH, '//*[@id="item_4_title_link"]/div')



    def selecionar_filtro_z_ao_a(self):
        self.driver.find_element(*self.catalog_filter).click()
        self.driver.find_element(*self.name_z_to_a).click 
    
    def selecionar_filtro_high_to_low(self):
        self.driver.find_element(*self.catalog_filter).click()
        self.driver.find_element(*self.price_high_to_low).click()
    
    def selecionar_filtro_low_to_high(self):
        self.driver.find_element(*self.catalog_filter).click()
        self.driver.find_element(*self.price_low_to_high).click()
    
    def abrir_descrição_do_produto(self):
        self.driver.find_element(*self.mochila).click()
    
    def voltar_ao_catalogo(self):
        self.driver.find_element(*self.mochila).click()
        self.driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()


        