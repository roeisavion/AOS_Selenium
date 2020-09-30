from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AOS_Selenium.Page import Page

class MyOrdersPage(Page) :
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def GetLastOrderNumber(self):
        orderNumbers=self.driver.find_elements_by_css_selector('tr>td:nth-child(1)>label')
        return orderNumbers[-1].text