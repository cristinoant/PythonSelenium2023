from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html"


class TestDownloadProgressPage:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.implicitly_wait(2)
        self.wait_driver = WebDriverWait(self.driver, 40)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_download_progress_page(self):
        # Find button Start Download and press clic
        button_start_download = self.__find_clickable_element(By.XPATH, '//button[@id="downloadButton"]')
        button_start_download.click()

        # Validate the mesagge Complete and button Close
        self.__find_by_text(By.XPATH, '//div[@class="progress-label"]', 'Complete!')
        self.__find_clickable_element(By.XPATH, '//button[contains(text(), "Close")]')

    def __find_clickable_element(self, by: By, value: str) -> WebElement:
        return self.wait_driver.until(EC.element_to_be_clickable((by, value)))

    def __find_by_text(self, by: By, value: str, text: str) -> WebElement:
        return self.wait_driver.until(EC.text_to_be_present_in_element((by, value), text))

    def teardown_method(self):
        self.driver.quit()
