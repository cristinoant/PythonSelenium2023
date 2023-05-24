import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://demoqa.com/select-menu"


class TestDemoQAPage:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_multi_select_menu(self):
        time.sleep(1)

        # Find element by visible value Volvo
        element = self.driver.find_element(By.ID, "cars")
        select_element_volvo = Select(element)
        select_element_volvo.select_by_visible_text("Volvo")

        # Send Press ctrl button in keyboard
        control_option = self.driver.find_element(By.ID, "cars")
        control_option.send_keys(Keys.CONTROL)

        # Find element by visible value Audi
        select_element_audi = Select(element)
        select_element_audi.select_by_visible_text("Audi")

        time.sleep(3)

    def teardown_method(self):
        self.driver.quit()
