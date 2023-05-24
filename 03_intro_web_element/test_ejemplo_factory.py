import time

from selenium.webdriver.common.by import By
from factory.webdriver_factory import get_driver

URL = "https://laboratorio.qaminds.com/"


class TestLaboratorioQAMinds:

    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(URL)

    def test_search_iphone(self):
        # Escribir Iphone
        search_input = self.driver.find_element(By.NAME, "search")
        assert search_input.is_displayed() and search_input.is_enabled(), "El campo de busqueda tiene que estar visible y habilitado"
        search_input.send_keys("Iphone")

        # Dar click en buscar
        search_btn = self.driver.find_element(By.XPATH, "//div[@id='search']//button")
        assert search_btn.is_displayed() and search_btn.is_enabled(), "El boton de busqueda tiene que estar visible y habilitado"
        search_btn.click()

        # Verificar resultados
        iphone_img = self.driver.find_element(By.XPATH, "//img[@alt='iPhone' and contains(@src, 'iphone')]")
        assert iphone_img.is_displayed(), "La imagen de Iphone tiene que estar en el DOM"

    def teardown_method(self):
        self.driver.quit()

