from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AOS_Selenium.Page_Objects.Page import Page


class CategoryPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def ProductInList(self,number_in_page):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,f"div.cell>ul>li.ng-scope:nth-child({number_in_page})")))
        return self.driver.find_element_by_css_selector(f"div.cell>ul>li.ng-scope:nth-child({number_in_page})")

    def ClickProduct(self,number_in_page):
        """Click on product"""
        self.ProductInList(number_in_page).click()

    def FindTitle(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located\
                                                 ((By.CLASS_NAME, "categoryTitle")))
        title = self.driver.find_element_by_class_name("categoryTitle")
        return title.text







