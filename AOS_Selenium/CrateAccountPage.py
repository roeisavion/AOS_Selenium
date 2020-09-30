from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from AOS_Selenium.Page import Page
from time import sleep

class CreateAccountPage(Page) :
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def Account_Username(self,username):
        self.driver.find_element_by_name("usernameRegisterPage").send_keys(username)

    def Account_Password(self,password):
        self.driver.find_element_by_name("passwordRegisterPage").send_keys(password)

    def Confirm_Password(self,password):
        self.driver.find_element_by_name("confirm_passwordRegisterPage").send_keys(password)

    def Account_Email(self,email):
        self.driver.find_element_by_name("emailRegisterPage").send_keys(email)

    def Click_I_Aggree(self):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element((By.CSS_SELECTOR, "ul>li>tool-tip-cart>div>table")))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "i_agree")))
        # sleep(2)
        self.driver.find_element_by_name("i_agree").click()

    def Click_Register(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,"register_btnundefined")))
        self.driver.find_element_by_id("register_btnundefined").click()