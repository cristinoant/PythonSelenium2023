import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://laboratorio.qaminds.com/"


class TestingLaboratorioQAMinds:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.get(URL)

    # Search on textbox
    def test_search_iphone(self):
        time.sleep(3)

        # Clic textbox
        search_textbox = self.driver.find_element(By.XPATH, '//input[@name="search"]')
        assert search_textbox.is_displayed(), "El textbox debe mostrarse"
        assert search_textbox.is_enabled(), "El textbox debe estar habilitado"
        search_textbox.click()
        time.sleep(2)
        search_textbox.send_keys("iPhone", Keys.ENTER)
        time.sleep(3)

        # Validate img result
        validate_img = self.driver.find_element(By.XPATH, "//img[@alt='iPhone']")
        assert validate_img.is_displayed(), "La imagen iPhone debe mostrarse"
        assert validate_img.is_enabled(), "La imagen debe estar habilitada"

    def teardown_method(self):
        self.driver.quit()
