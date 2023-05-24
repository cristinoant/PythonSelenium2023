from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://demo.seleniumeasy.com/bootstrap-alert-messages-demo.html"


class TestDownloadProgressPage:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.implicitly_wait(2)
        self.wait_driver = WebDriverWait(self.driver, 40)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_autoclose_message(self):
        # Find button Autoclosable and press click
        button_autoclose = self.__find_clickable_element(By.XPATH, '//button[@id="autoclosable-btn-success"]')
        button_autoclose.click()

        # Validate the message is visible
        self.__find_visible_element(By.XPATH, '//div[contains(text(), "I\'m an autocloseable success  message. I will hide in 5 seconds.")]')

        # Validate the message dissappears
        self.__wait_until_disappears(By.XPATH, '//div[contains(text(), "I\'m an autocloseable success  message. I will hide in 5 seconds.")]')

    def __find_clickable_element(self, by: By, value: str) -> WebElement:
        return self.wait_driver.until(EC.element_to_be_clickable((by, value)))

    def __find_visible_element(self, by: By, value: str) -> WebElement:
        return self.wait_driver.until(EC.visibility_of_element_located((by, value)))

    def __wait_until_disappears(self, by: By, value: str):
        self.wait_driver.until(EC.invisibility_of_element((by, value)))

    def teardown_method(self):
        self.driver.quit()
