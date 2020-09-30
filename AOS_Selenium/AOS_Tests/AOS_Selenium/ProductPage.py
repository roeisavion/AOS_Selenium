from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidSelectorException
from AOS_Selenium.Page import Page


class ProductPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def Set_Quantity(self, quantity):
        """Set quantity of product"""
        self.driver.find_element_by_css_selector("input[numbers-only='""']").click()
        self.driver.find_element_by_css_selector("input[numbers-only='""']").send_keys(str(quantity))

    def color(self, COLOR_IN_CAPITALS):
        """Return color element"""
        return self.driver.find_element_by_css_selector(f"div[class =''] >.productColor[title='{COLOR_IN_CAPITALS}']")

    def choose_color(self, COLOR_IN_CAPITALS):
        """Click on color """
        self.color(COLOR_IN_CAPITALS).click()

    def Click_Add_To_Cart(self):
        """Adding product to cart"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located \
                                                  ((By.CSS_SELECTOR, "button[translate='ADD_TO_CART']")))

        self.driver.find_element_by_css_selector("button[translate='ADD_TO_CART']").click()

    def GetName(self):
        """Return product name"""
        return self.driver.find_element_by_css_selector("h1[class='roboto-regular screen768 ng-binding']").text

    def GetPrice(self):
        """Return product price"""
        price = self.driver.find_element_by_xpath("//div[@id='Description']/h2[@class='roboto-thin screen768 ng-binding']").text
        if price[0] == '$':
            price = price[1:]
            return price
        return price

    def GetQuantity(self):
        """Returns the quantity I set on a product page"""
        Quantity = self.driver.find_element_by_css_selector("input[numbers-only='""']").get_attribute("value")
        return Quantity

    def GetSelectedColor(self):
        """Returns the color I set on a product page"""
        try:
            color = self.driver.find_element_by_css_selector("span#rabbit.colorSelected")
        except InvalidSelectorException:
            color = self.driver.find_element_by_css_selector("span#bunny.colorSelected")

        return color.get_attribute("title")

    def GetProductDetails(self):
        """Returns the product details I selected, the color, and the quantity"""
        name = self.GetName()
        color = self.GetSelectedColor()
        QTY = self.GetQuantity()
        price = self.GetPrice()
        ProductDetails= f'Name= {name} ,Color= {color},Quantity= {int(QTY)},Price= {(float(price))*(int(QTY))}'
        return ProductDetails






















