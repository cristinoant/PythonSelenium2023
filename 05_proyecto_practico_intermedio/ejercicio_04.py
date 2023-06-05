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

        # Buscar Elemento Samsung
        search_box = self.__find_clickable_element(By.NAME, "search")
        search_box.click()

        search_box.send_keys("Samsung SyncMaster 941BW")
        search_box.send_keys(Keys.ENTER)

        # Clic in element Samsung SyncMaster
        element = self.__find_clickable_element(By.PARTIAL_LINK_TEXT, 'Samsung SyncMaster 941BW')
        element.click()

        # Find button Currency
        currency_button = self.__find_clickable_element(By.XPATH, '//*[@id="form-currency"]//button/span')
        currency_button.click()

        # Select Currency USD
        currency_usd = self.__find_clickable_element(By.XPATH, '//button[@name="USD"]')
        currency_usd.click()

        time.sleep(2)

        # Guardar el precio en USD
        precio_usd = self.__find_visible_element(By.XPATH, '//h2[contains(text(), "$242.00")]').text

        # Buscar botton Currency
        currency = self.__find_visible_element(By.XPATH, '//*[@id="form-currency"]//button/span')
        currency.click()

        # Seleccionar Euro
        currency_euro = self.__find_visible_element(By.XPATH, '//button[@name="EUR"]')
        currency_euro.click()

        precio_euro = self.__find_visible_element(By.XPATH, '//h2[contains(text(), "189.87€")]').text

        # Validate price elements USD is more expensive
        assert precio_usd.replace("$", "") > precio_euro.replace("€", ""), "The price in USD should be expensive than Euro"

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
