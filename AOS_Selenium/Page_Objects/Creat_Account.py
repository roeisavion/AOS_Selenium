from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from AOS_Selenium.Page_Objects.Page import Page
from selenium.webdriver.support.ui import Select
from random import randint


class CreateAccount(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def find_username(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "usernameRegisterPage")))
        return self.driver.find_element_by_name("usernameRegisterPage")

    def find_password(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='passwordRegisterPage']")))
        return self.driver.find_element_by_css_selector("input[name='passwordRegisterPage']")

    def find_confirm_password(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='confirm_passwordRegisterPage']")))
        return self.driver.find_element_by_css_selector("input[name='confirm_passwordRegisterPage']")

    def find_email(self):
        return self.driver.find_element_by_name("emailRegisterPage")

    def find_first_name(self):
        return self.driver.find_element_by_name("first_nameRegisterPage")

    def find_last_name(self):
        return self.driver.find_element_by_name("last_nameRegisterPage")

    def find_phone_number(self):
        return self.driver.find_element_by_name("phone_numberRegisterPage")

    def find_country_dropdown(self):
        select = Select(self.driver.find_element_by_css_selector("select[role='listbox']"))
        return select

    def find_city(self):
        return self.driver.find_element_by_name("cityRegisterPage")

    def find_address(self):

        return self.driver.find_element_by_name("addressRegisterPage")

    def find_region(self):
        return self.driver.find_element_by_name("state_/_province_/_regionRegisterPage")

    def find_postal_code(self):
        return self.driver.find_element_by_name("postal_codeRegisterPage")

    def find_check_box(self):
        element = (self.driver.find_element_by_name("i_agree"))
        actionChains = ActionChains(self.driver)
        actionChains.move_to_element(element).perform()
        return element

    def find_register_button(self):
        return self.driver.find_element_by_css_selector("button#register_btnundefined")

    def register_account(self):
        """Register a new account"""
        # self.find_username().send_keys(str(uuid4())[:14])   # alternative option for random username
        self.find_username().send_keys("maor90a"+str(randint(1, 100000)))
        self.find_password().send_keys("12345aA")
        self.find_confirm_password().send_keys("12345aA")
        self.find_email().send_keys("maor20b@gmail.com")
        self.find_first_name().send_keys("Maor")
        self.find_last_name().send_keys("Bartov")
        self.find_phone_number().send_keys("0501234567")
        self.find_country_dropdown().select_by_visible_text('Israel')
        self.find_city().send_keys("Holon")
        self.find_address().send_keys("Laskov Haim 27")
        self.find_region().send_keys("TLV")
        self.find_postal_code().send_keys("52718")
        self.find_check_box().click()
        self.find_register_button().click()






