from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from factory.webdriver_factory import get_driver

URL = "https://laboratorio.qaminds.com"


class TestLaboratorioQAMinds:

    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(URL)
        self.wait_driver = WebDriverWait(self.driver, 15)

    def test_open_landing_page(self):

        # Validate image Home Page
        self.__find_visible_element(By.XPATH, '//img[@title="Your Store"]')

        # Method to validate the element is visible
    def __find_visible_element(self, by: By, value: str) -> WebElement:
        return self.wait_driver.until(EC.visibility_of_element_located((by, value)))

    def teardown_method(self):
        self.driver.quit()
