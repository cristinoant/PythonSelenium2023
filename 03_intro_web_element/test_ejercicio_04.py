import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://laboratorio.qaminds.com"


class TestingLaboratorioQAMinds:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_validate_option_windows(self):
        # Move the mouse to Element Laptops & Notebooks
        hover_mouse = self.driver.find_element(By.XPATH, '//a[contains(text(), "Laptops & Notebooks")]')
        ActionChains(self.driver).move_to_element(hover_mouse).perform()
        time.sleep(5)

        # Find element Windows
        find_windows_element = self.driver.find_element(By.XPATH, '//a[contains(text(), "Windows")]')
        find_windows_element.click()
        time.sleep(3)

        # Validate element is displayed and enabled
        find_label = self.driver.find_element(By.XPATH, '//div[@id="content"]/p')
        assert find_label.is_displayed(), "El elemento debe ser visible"
        assert find_label.is_enabled(), "El elemento debe ser habilitado"

        # Press button to continue
        btn_continue = self.driver.find_element(By.XPATH, '//a[@class="btn btn-primary"]')
        btn_continue.click()

        time.sleep(3)

    def tear_down(self):
        self.driver.quit()
        