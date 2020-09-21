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

    def FindUsername(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "usernameRegisterPage")))
        return self.driver.find_element_by_name("usernameRegisterPage")

    def FindPassWord(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='passwordRegisterPage']")))
        return self.driver.find_element_by_css_selector("input[name='passwordRegisterPage']")

    def FindConfirmPassWord(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='confirm_passwordRegisterPage']")))
        return self.driver.find_element_by_css_selector("input[name='confirm_passwordRegisterPage']")

    def FindEmail(self):
        return self.driver.find_element_by_name("emailRegisterPage")

    def FindFirstName(self):
        return self.driver.find_element_by_name("first_nameRegisterPage")

    def FindLastName(self):
        return self.driver.find_element_by_name("last_nameRegisterPage")

    def FindPhoneNumber(self):
        return self.driver.find_element_by_name("phone_numberRegisterPage")

    def FindCountryDropDown(self):
        select = Select(self.driver.find_element_by_css_selector("select[role='listbox']"))
        return select

    def FindCity(self):
        return self.driver.find_element_by_name("cityRegisterPage")

    def FindAddress(self):

        return self.driver.find_element_by_name("addressRegisterPage")

    def FindRegion(self):
        return self.driver.find_element_by_name("state_/_province_/_regionRegisterPage")

    def FindPostalCode(self):
        return self.driver.find_element_by_name("postal_codeRegisterPage")

    def FindCheckbox(self):
        element = (self.driver.find_element_by_name("i_agree"))
        actionChains = ActionChains(self.driver)
        actionChains.move_to_element(element).perform()
        return element

    def FindRegisterButton(self):
        return self.driver.find_element_by_css_selector("button#register_btnundefined")


    def RegisterAnAccount(self):
        """Register a new account"""
        # self.FindUsername().send_keys(str(uuid4())[:14])
        self.FindUsername().send_keys("maor90a"+str(randint(1, 100000)))
        self.FindPassWord().send_keys("12345aA")
        self.FindConfirmPassWord().send_keys("12345aA")
        self.FindEmail().send_keys("maor20b@gmail.com")
        self.FindFirstName().send_keys("Maor")
        self.FindLastName().send_keys("Bartov")
        self.FindPhoneNumber().send_keys("0501234567")
        self.FindCountryDropDown().select_by_visible_text('Israel')
        self.FindCity().send_keys("Holon")
        self.FindAddress().send_keys("Laskov Haim 27")
        self.FindRegion().send_keys("TLV")
        self.FindPostalCode().send_keys("52718")
        self.FindCheckbox().click()
        self.FindRegisterButton().click()






