import time
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from factory.webdriver_factory import get_driver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

URL = "https://laboratorio.qaminds.com/index.php?route=account/login"


class TestLaboratorioQAMinds:

    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(URL)
        self.wait_driver = WebDriverWait(self.driver, 15)

    def test_add_multi_items_to_cart(self):
        # Loggin to the page
        email_user = self.__find_clickable_element(By.XPATH, '//input[@id="input-email"]')
        email_user.click()
        email_user.send_keys("cristinoant@hotmail.com")

        password_user = self.__find_clickable_element(By.XPATH, '//input[@id="input-password"]')
        password_user.click()
        password_user.send_keys("qamindslab.")
        password_user.send_keys(Keys.ENTER)

        # Validate currency USD
        currency_button = self.__find_clickable_element(By.XPATH, '//*[@id="form-currency"]//button')
        currency_button.click()

        # Select USD
        currency_usd = self.__find_clickable_element(By.XPATH, '//button[@name="USD"]')
        currency_usd.click()

        # Find in the Menu "MP3 Players"
        mover_mouse = self.__find_visible_element(By.XPATH, '//a[contains(text(), "MP3 Players")]')
        ActionChains(self.driver).move_to_element(mover_mouse).perform()

        # Select Show All
        show_all_mp3 = self.__find_clickable_element(By.XPATH, '//a[contains(text(), "Show All MP3 Players")]')
        show_all_mp3.click()

        # Verify show 4 elements
        self.__find_visible_element(By.LINK_TEXT, 'iPod Classic')
        self.__find_visible_element(By.LINK_TEXT, 'iPod Nano')
        self.__find_visible_element(By.LINK_TEXT, 'iPod Shuffle')
        self.__find_visible_element(By.LINK_TEXT, 'iPod Touch')

        # Add to cart every element
        add_to_cart_ipod_classic = self.__find_clickable_element(By.XPATH, '//*[@onclick="cart.add(\'48\', \'1\');"]')
        add_to_cart_ipod_classic.click()

        add_to_cart_ipod_nano = self.__find_clickable_element(By.XPATH, '//*[@onclick="cart.add(\'36\', \'1\');"]')
        add_to_cart_ipod_nano.click()

        time.sleep(2)

        add_to_cart_ipod_shuffle = self.__find_clickable_element(By.XPATH, '//*[@onclick="cart.add(\'34\', \'1\');"]')
        add_to_cart_ipod_shuffle.click()

        add_to_cart_ipod_touch = self.__find_clickable_element(By.XPATH, '//*[@onclick="cart.add(\'32\', \'1\');"]')
        add_to_cart_ipod_touch.click()

        # Validate checkout
        validate_checkout = self.__find_clickable_element(By.XPATH, '//*/span[@id="cart-total"]')
        validate_checkout.click()

        time.sleep(1)

        # Validar the elements in cart
        self.__find_visible_element(By.XPATH, '//td/a/img[@alt="iPod Classic"]')
        self.__find_visible_element(By.XPATH, '//td/a/img[@alt="iPod Nano"]')
        self.__find_visible_element(By.XPATH, '//td/a/img[@alt="iPod Shuffle"]')
        self.__find_visible_element(By.XPATH, '//td/a/img[@alt="iPod Touch"]')

        # Validate subtotal amount
        self.__find_by_text(By.XPATH, '//*/div/table/tbody/tr[1]/td[2]', "$400.00")

        # Validate total amount
        self.__find_by_text(By.XPATH, '//*/div/table/tbody/tr[2]/td[2]', "$400.00")

        time.sleep(1)

        # Press the button Checkout
        button_checkout = self.__find_clickable_element(By.LINK_TEXT, 'Checkout')
        button_checkout.click()

        # Press button "I want to use a new address"
        btn_new_billing = self.__find_clickable_element(By.XPATH, '//*/input[@name="payment_address" and @value="new"]')
        btn_new_billing.click()

        # Fill the address
        self.__find_visible_element(By.ID, 'input-payment-firstname').send_keys("Jose")
        self.__find_visible_element(By.ID, 'input-payment-lastname').send_keys("Perez")
        self.__find_visible_element(By.ID, 'input-payment-company').send_keys("QA Minds")
        self.__find_visible_element(By.ID, 'input-payment-address-1').send_keys("Calle Centro")
        self.__find_visible_element(By.ID, 'input-payment-city').send_keys("Mexico")
        self.__find_visible_element(By.ID, 'input-payment-postcode').send_keys("09440")

        country = self.driver.find_element(By.ID, "input-payment-country")
        select = Select(country)
        select.select_by_value("138")

        state = self.driver.find_element(By.ID, "input-payment-zone")
        select = Select(state)
        select.select_by_value("2153")

        # Press button Continue
        continue_btn_payment = self.__find_clickable_element(By.ID, 'button-payment-address')
        continue_btn_payment.click()

        # Select existing address
        self.__find_clickable_element(By.XPATH, '//*/input[@name="shipping_address" and @value="existing"]')
        continue_btn_adress = self.__find_clickable_element(By.ID, 'button-shipping-address')
        continue_btn_adress.click()

        # Press button Continue
        continue_btn_method = self.__find_clickable_element(By.ID, 'button-shipping-method')
        continue_btn_method.click()

        # Press button Terms & Conditions
        checkbox_agree = self.__find_clickable_element(By.NAME, "agree")
        checkbox_agree.click()

        # Press button Continue
        contiue_btn_payment_method = self.__find_clickable_element(By.ID, 'button-payment-method')
        contiue_btn_payment_method.click()

        # Press button Confirm Order
        confirm_order = self.__find_clickable_element(By.ID, 'button-confirm')
        confirm_order.click()

        time.sleep(1)

    def __find_clickable_element(self, by: By, value: str) -> WebElement:
        return self.wait_driver.until(EC.element_to_be_clickable((by, value)))

    def __find_visible_element(self, by: By, value: str) -> WebElement:
        return self.wait_driver.until(EC.visibility_of_element_located((by, value)))

    def __find_by_text(self, by: By, value: str, text: str) -> WebElement:
        return self.wait_driver.until(EC.text_to_be_present_in_element((by, value), text))
