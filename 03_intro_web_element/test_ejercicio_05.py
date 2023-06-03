from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://laboratorio.qaminds.com"


class TestingLaboratorioQAMinds:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_validate_items(self):
        # Validate the items and price be displayed
        macbook_item = self.driver.find_element(By.LINK_TEXT, 'MacBook')
        macbook_item.click()
        macbook_price = self.driver.find_element(By.XPATH, '//h2[contains(text(), "$602.00")]').text
        assert macbook_price == '$602.00', "The price should be $602.00"

        self.driver.back()

        iphone_item = self.driver.find_element(By.LINK_TEXT, 'iPhone')
        iphone_item.click()
        iphone_price = self.driver.find_element(By.XPATH, '//h2[contains(text(), "$123.20")]').text
        assert iphone_price == '$123.20', "The price should be $123.20"

        self.driver.back()

        apple_cinema = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Apple Cinema')
        apple_cinema.click()
        apple_cinema_price = self.driver.find_element(By.XPATH, '//h2[contains(text(), "$110.00")]').text
        assert apple_cinema_price == '$110.00', "The price should be $110.00"

        self.driver.back()

        canon = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Canon')
        canon.click()
        canon_price = self.driver.find_element(By.XPATH, '//h2[contains(text(), "$98.00")]').text
        assert canon_price == '$98.00', "The price should be $98.00"

        self.driver.back()

    def tear_down(self):
        self.driver.quit()
        