from AOS_Selenium.Page_Objects.Page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GuestUser(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    def FindUsername(self):
        """Find UserName element"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located
                                             ((By.NAME, "username")))
        return self.driver.find_element_by_name("username")

    def FindPassWord(self):
        """Find PassWord element"""
        return self.driver.find_element_by_name("password")

    def SignIn(self, username= 'maor90b8989', password='12345aA'):
        """Account login"""
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element
                                             ((By.CSS_SELECTOR, ".loader:nth-child(1)")))
        self.UserIconClick()
        self.FindUsername().send_keys(username)
        self.FindPassWord().send_keys(password)
        self.driver.find_element_by_id("sign_in_btnundefined").click()

