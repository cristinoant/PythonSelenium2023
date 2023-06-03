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

    def test_search_products(self):
        # Search Display
        search_input = self.__find_clickable_element(By.NAME, "search")
        search_input.send_keys("Display")
        search_input.send_keys(Keys.ENTER)

        # Validate the lable is visible after the search
        self.__find_visible_element(By.XPATH, '//p[contains(text(),"There is no product")]')

        # Press the checkbox
        press_checkbox = self.__find_clickable_element(By.XPATH, '//input[@name="description"]')
        press_checkbox.click()

        # Find the element again
        button_search = self.__find_clickable_element(By.XPATH, '//input[@id="button-search"]')
        button_search.click()

        # Validate the results
        self.__find_visible_element(By.XPATH, '//a[contains(text(), "Apple Cinema 30")]')
        self.__find_visible_element(By.XPATH, '//a[contains(text(), "iPod Nano")]')
        self.__find_visible_element(By.XPATH, '//a[contains(text(), "iPod Touch")]')
        self.__find_visible_element(By.XPATH, '//a[contains(text(), "MacBook Pro")]')

    # Method to validate the element is clickable
    def __find_clickable_element(self, by: By, value: str) -> WebElement:
        return self.wait_driver.until(EC.element_to_be_clickable((by, value)))

    # Method to validate the element is visible
    def __find_visible_element(self, by: By, value: str) -> WebElement:
        return self.wait_driver.until(EC.visibility_of_element_located((by, value)))

    def teardown(self):
        self.driver.quit()
