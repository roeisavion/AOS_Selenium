from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AOS_Selenium.Page import Page
from AOS_Selenium.ProductPage import ProductPage

class CategoryPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def productInList(self,number_in_page):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,f"div.cell>ul>li.ng-scope:nth-child({number_in_page})")))
        return self.driver.find_element_by_css_selector(f"div.cell>ul>li.ng-scope:nth-child({number_in_page})")

    def clickProduct(self,number_in_page):
        """Click on product"""
        self.productInList(number_in_page).click()

    def add_product_to_cart_category_page(self,number_in_page,COLOR_IN_CAPITALS,quantity):
        self.clickProduct(number_in_page)
        self.pp2=ProductPage(self.driver)
        self.pp2.choose_color(COLOR_IN_CAPITALS)
        self.pp2.Set_Quantity(quantity)
        self.pp2.Click_Add_To_Cart()
        self.driver.back()

