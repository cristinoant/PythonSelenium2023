from selenium.webdriver import ActionChains
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

    def test_add_to_cart(self):
        # Move Mouse to option Desktop
        mover_mouse = self.__find_visible_element(By.XPATH, '//a[contains(text(), "Desktops")]')
        ActionChains(self.driver).move_to_element(mover_mouse).perform()

        # Select Mac
        find_mac_element = self.__find_clickable_element(By.XPATH, '//a[contains(text(), "Mac")]')
        find_mac_element.click()

        # Validate item iMac
        self.__find_visible_element(By.XPATH, '//a[contains(text(), "iMac")]')

        # Add to cart
        add_to_cart = self.__find_clickable_element(By.XPATH, '//*[contains(@onclick, "cart.add")]')
        add_to_cart.click()

        # Validate add to cart and validate the text
        self.__find_by_text(By.ID, 'cart-total', '1 item(s) - $122.00')

    # Method to validate the element is clickable
    def __find_clickable_element(self, by: By, value: str) -> WebElement:
        return self.wait_driver.until(EC.element_to_be_clickable((by, value)))

    # Method to validate the element is visible
    def __find_visible_element(self, by: By, value: str) -> WebElement:
        return self.wait_driver.until(EC.visibility_of_element_located((by, value)))

    # Method to validate the text of the element
    def __find_by_text(self, by: By, value: str, text: str) -> WebElement:
        return self.wait_driver.until(EC.text_to_be_present_in_element((by, value), text))

    def teardown(self):
        self.driver.quit()
