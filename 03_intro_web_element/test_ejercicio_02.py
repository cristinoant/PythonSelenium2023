import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://laboratorio.qaminds.com/"


class TestingLaboratorioQAMinds:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_search_tablets(self):
        time.sleep(2)
        # Select option Tablets
        search_tablet = self.driver.find_element(By.XPATH, '//*[contains(a, "Tablets")]')
        assert search_tablet.is_displayed(), "El elemento Tablet debe ser visible"
        assert search_tablet.is_enabled(), "El elemento Tablet debe estar habilitado"
        search_tablet.click()

        time.sleep(2)
        # Validate show item with title: Samsung Galaxy Tab 10.1
        locate_tablet = self.driver.find_element(By.XPATH, '//img[@alt="Samsung Galaxy Tab 10.1"]')
        assert locate_tablet.is_displayed(), "El elemento Galaxy debe ser visible"
        assert locate_tablet.is_enabled(), "El elemento Galaxy debe estar habilitado"

        # Select Item
        locate_tablet.click()
        time.sleep(2)

        # Validate the cost equals: $241.99
        cost_table = self.driver.find_element(By.XPATH, '//li/h2[text() = "$241.99"]').text
        assert cost_table == "$241.99", "El costo de la tablet debe ser $241.99"

        # Add to Whish List
        add_wishlist = self.driver.find_element(By.XPATH, '//button[@data-original-title="Add to Wish List"]')
        assert add_wishlist.is_displayed(), "El boton Wishlist debe ser visible"
        assert add_wishlist.is_enabled(), "El boton Wishlist debe estar habilitado"

        # Select Item
        add_wishlist.click()
        time.sleep(2)

        # Validate add to Whitelist correctly
        validate_wishlist = self.driver.find_element(By.XPATH, '//span[contains(text(), "Wish List (1)")]').text
        assert validate_wishlist == "Wish List (1)", "El texto debe ser > 0"

        # Add to cart
        add_cart = self.driver.find_element(By.XPATH, '//button[@id="button-cart"]')
        assert add_cart.is_enabled() and add_cart.is_displayed(), "El boton Add to Cart debe estar visible y habilitado"
        add_cart.click()
        time.sleep(3)

        # Validate add to cart correctly
        validate_cart = self.driver.find_element(By.XPATH, '//span[@id="cart-total"]').text
        assert validate_cart == "1 item(s) - $241.99", "El n° de Items debe ser 1 y el precio debe ser $241.99"

    def teardown_method(self):
        self.driver.quit()
