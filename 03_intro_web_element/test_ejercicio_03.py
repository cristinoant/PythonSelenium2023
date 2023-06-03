import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://laboratorio.qaminds.com/index.php?route=account/login"


class TestingLaboratorioQAMinds:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_invalid_login(self):
        # Login to app with email
        email_login = self.driver.find_element(By.XPATH, '//input[@name="email"]')
        assert email_login.is_displayed(), "El textbox debe mostrarse"
        assert email_login.is_enabled(), "El textbox debe estar habilitado"
        email_login.click()
        time.sleep(2)
        email_login.send_keys("email@email.com")

        # Login to app with pass
        pass_login = self.driver.find_element(By.XPATH, '//input[@name="password"]')
        assert pass_login.is_displayed(), "El textbox debe mostrarse"
        assert pass_login.is_enabled(), "El textbox debe estar habilitado"
        pass_login.click()
        time.sleep(2)
        pass_login.send_keys("password123")

        # Press button Login
        btn_login = self.driver.find_element(By.XPATH, '//input[@class="btn btn-primary"]')
        assert btn_login.is_displayed(), "El textbox debe mostrarse"
        assert btn_login.is_enabled(), "El textbox debe estar habilitado"
        btn_login.click()

        # Validate message error
        message_error = self.driver.find_element(By.XPATH, '//*[contains(text(), "Warning")]')
        assert message_error.is_displayed(), "El mensaje de Warning debe mostrarse"
        assert message_error.is_enabled(), "El mensaje de Warning debe mostrarse"

        # TODO
        # Realizar validacion con diferentes usuarios
        # Usuario valido, usuario invalido, usuario con formato invalido de correo

    def teardown_method(self):
        self.driver.quit()
