import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from factory.webdriver_factory import get_driver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = "https://laboratorio.qaminds.com/"


class TestLaboratorioQAMinds:

    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(URL)
        self.wait_driver = WebDriverWait(self.driver, 15)

    def test_validate_currency(self):
        # Buscar boton Currency
        currency_button = self.__find_clickable_element(By.XPATH, '//*[@id="form-currency"]//button')
        currency_button.click()

        # Seleccionar USD
        currency_usd = self.__find_clickable_element(By.XPATH, '//button[@name="USD"]')
        currency_usd.click()

        # Buscar Elemento Samsung
        search_box = self.__find_clickable_element(By.NAME, "search")
        search_box.click()

        search_box.send_keys("Samsung SyncMaster 941BW")
        search_box.send_keys(Keys.ENTER)

        # Guardar el precio en USD
        precio_usd = self.__find_by_text(By.XPATH, '//p[@class="price"][1]', '$242.00')

        # Buscar botton Currency
        currency = self.driver.find_element(By.XPATH, '//*[@id="form-currency"]//button/span')
        currency.click()

        # Seleccionar Euro
        currency_euro = self.driver.find_element(By.XPATH, '//button[@name="EUR"]')
        currency_euro.click()

        # Guardar el precio en Euro
        precio_euro = self.__find_by_text(By.XPATH, '//p[@class="price"][1]', '189.87€')

        validate_precio_euro = self.driver.find_element(By.XPATH, '//p[@class="price"]').text

        ##assert validate_wishlist == "Wish List (1)", "El texto debe ser > 0"



        print("*****")
        print(validate_precio_euro)
        #print(precio_usd)
        print("*****")

        #time.sleep(3)

    def __find_clickable_element(self, by: By, value: str) -> WebElement:
        return self.wait_driver.until(EC.element_to_be_clickable((by, value)))

    def __find_visible_element(self, by: By, value: str) -> WebElement:
        return self.wait_driver.until(EC.visibility_of_element_located((by, value)))

    def __find_by_text(self, by: By, value: str, text: str) -> WebElement:
        return self.wait_driver.until(EC.text_to_be_present_in_element((by, value), text))

    def __wait_until_disappears(self, by: By, value: str):
        self.wait_driver.until(EC.invisibility_of_element((by, value)))


    def teardown(self):
        self.driver.quit()
