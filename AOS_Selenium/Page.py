from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from time import sleep
from selenium.webdriver.remote.webelement import WebElement


class Page():
    """Class 'Page' holds simple functions for page"""
    def __init__(self, driver):
        self.driver = driver

    def UserIconClick(self):
        """Click on user icon"""
        self.driver.find_element_by_id("menuUser").click()

    def MyOrdersClick(self):
        self.UserIconClick()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable \
                                                 ((By.CSS_SELECTOR, 'a>div>label[translate="My_Orders"]')))
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, 'label[translate="Your_shopping_cart_is_empty"]')))
        self.driver.find_element_by_css_selector('a>div>label[translate="My_Orders"]').click()

    def FindUsername(self):
        """Find UserName element"""
        self.driver.find_element_by_name("username")

    def FindPassWord(self):
        """Find PassWord element"""
        self.driver.find_element_by_name("password")

    def SignIn(self, username, password):
        """Account login"""
        self.FindUsername().send_keys(username)
        self.FindPassWord().send_keys(password)
        self.driver.find_element_by_id("sign_in_btnundefined").click()

    def FindCart(self):
        """Find 'Cart' icon element"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located \
                                                 ((By.ID, "menuCart")))
        return self.driver.find_element_by_id("menuCart")

    def MouseOnIconCart(self):
        """Put mouse on 'Cart' icon"""
        cart = self.driver.find_element_by_id("menuCart")
        actionChains = ActionChains(self.driver)
        actionChains.move_to_element(cart).perform()

    def CheckEmptyCart(self):
        '''returns true or false depends if the cart empty or not'''
        self.MouseOnIconCart()
        # sleep(2)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'label[translate="Your_shopping_cart_is_empty"]')))
        return  self.driver.find_element_by_css_selector('label[translate="Your_shopping_cart_is_empty"]').is_displayed()


    def CartClick(self):
        """CLick on 'Cart' icon"""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable \
                                                 ((By.ID, "menuCart")))
        self.FindCart().click()

    def ClickOnCheckout(self):
        self.MouseOnIconCart()
        self.driver.find_element_by_name("check_out_btn").click()

    def ClickOnMyOrders(self):
        self.UserIconClick()
        self.driver.find_element_by_css_selector('''label[ng-click="mobileRedirect('MyOrders')"][role="link"]''').click()



    def CartTotalQuantity(self):
        """Return total of 'Cart' items"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located \
                                                  ((By.XPATH, "//label[@class='roboto-regular ng-binding']")))

        text = self.driver.find_element_by_xpath("//label[@class='roboto-regular ng-binding']").text
        EndNumIndex = text.index(' ')
        Quantity= text[1:EndNumIndex]
        NumOfProd=int(Quantity)
        return NumOfProd

    def GetProductQuantityFromCart(self, index):
        """Return specific product quantity in cart"""
        Quantities = self.driver.find_elements_by_xpath("//label[contains(text(), 'QTY')] ")
        Qty_of_Prod = int(Quantities[index].text[5:])
        return Qty_of_Prod



    def GetCartDetails(self):
        """Return dictionary of the products and their: name, color, quantity, price"""

        table = self.driver.find_element_by_css_selector('ul>li>tool-tip-cart>div>table>tbody')
        rows = table.find_elements_by_tag_name('tr')
        products = {}
        i = 1
        self.MouseOnIconCart()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located \
                                                 ((By.CSS_SELECTOR, "table[class='""']")))

        sleep(2)
        for row in rows:
            name = row.find_element_by_css_selector('tbody>tr>td>a>h3').text
            QTY = row.find_element_by_css_selector('tbody>tr>td>a>label').text
            color = row.find_element_by_css_selector('tbody>tr>td>a>label>span').text
            price = row.find_element_by_css_selector('tbody>tr>td>p').text
            for char in price:
                if char ==',':
                    price=price.replace(char, '')
            products[i] = (f'Name= {name} ,Color= {color},Quantity= {int(QTY[5:])},Price= {price[1:]}')
            i += 1
        return products


    def RemoveProductFromCart(self,index=0):
        """Remove one product from cart"""
        removes = self.driver.find_elements_by_css_selector('.removeProduct')
        if index > len(removes)-1:
            index =len(removes)-1
        removes[index].click()





















