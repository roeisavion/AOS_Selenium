from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from time import sleep



class Page():
    """Class 'Page' holds simple functions for page"""

    def __init__(self, driver):
        self.driver = driver

    def BackToMainPage(self):
        self.driver.find_element_by_css_selector("a[ng-click='go_up()']").click()

# Icon Cart Functions
    def FindCart(self):
        """Find 'Cart' icon element"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located \
                                                 ((By.ID, "menuCart")))
        return self.driver.find_element_by_id("menuCart")

    def MouseOnIconCart(self):
        """Put mouse on 'Cart' icon"""
        cart = self.FindCart()
        actionChains = ActionChains(self.driver)
        actionChains.move_to_element(cart).perform()

    def CartClick(self):
        """CLick on 'Cart' icon"""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable \
                                                 ((By.ID, "menuCart")))
        self.FindCart().click()

    def CartTotalQuantity(self):
        """Return total of 'Cart' items"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located \
                                                 ((By.XPATH, "//label[@class='roboto-regular ng-binding']")))
        text = self.driver.find_element_by_xpath("//label[@class='roboto-regular ng-binding']").text
        EndNumIndex = text.index(' ')
        Quantity = text[1:EndNumIndex]
        NumOfProd = int(Quantity)
        return NumOfProd

    def GetProductQuantityFromCart(self, index):
        """Return specific product quantity in cart"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located \
                                                 ((By.XPATH, "//label[contains(text(), 'QTY')]")))
        Quantities = self.driver.find_elements_by_xpath("//label[contains(text(), 'QTY')] ")
        Qty_of_Prod = int(Quantities[index].text[5:])
        return Qty_of_Prod


    def GetCartDetails(self):
        """Return dictionary of the products and their: name, color, quantity, price"""
        table = self.driver.find_element_by_tag_name('tbody')
        rows = table.find_elements_by_tag_name('tr')
        products = {}
        i = 1
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located \
                                                 ((By.TAG_NAME, "tbody")))
        for row in rows:
            name = row.find_element_by_css_selector('td>a>h3').text
            QTY = row.find_element_by_css_selector('td>a>label').text
            color = row.find_element_by_css_selector('td>a>label>span').text
            price = row.find_element_by_css_selector('td>p').text
            for char in price:
                if char == ',':
                    price = price.replace(char, '')
            for char2 in name:
                if char2=='.':
                    name=name.replace(char2,'')
            products[i] = (f'Name= {name} ,Color= {color},Quantity= {int(QTY[5:])},Price= {price[1:]}')
            i += 1
        return products


    def RemoveProductFromCart(self, index=0):
        """Remove one product from cart"""
        removes = self.driver.find_elements_by_css_selector('.removeProduct')
        if index > len(removes) - 1:
            index = len(removes) - 1
        removes[index].click()

    def FindCheckOut(self):
        """Return CheckOut button element"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located \
                                                 ((By.ID, "checkOutPopUp")))
        return self.driver.find_element_by_id("checkOutPopUp")

    def ClickCheckOut(self):
        """Clicking CheckOut button"""
        self.FindCheckOut().click()

    def FindCartIsEmpty(self):
        self.MouseOnIconCart()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located \
                                                 ((By.CSS_SELECTOR, "div.emptyCart")))
        return self.driver.find_element_by_css_selector("div.emptyCart").text

# User is not connected functions
    def UserIconClick(self):
        """Click on user icon"""
        sleep(2)
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element
                                             ((By.CSS_SELECTOR, ".loader:nth-child(1)")))
        WebDriverWait(self.driver,10).until(EC.invisibility_of_element
                                            ((By.CSS_SELECTOR, ".loader:nth-child(2)")))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable
                                            ((By.CSS_SELECTOR, "#menuUser")))
        user_icon = self.driver.find_element_by_css_selector("#menuUser")
        actionChains = ActionChains(self.driver)
        actionChains.move_to_element(user_icon)
        user_icon.click()

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


# User is connected functions
    def SeeMyorders(self):
        """Click on 'My Orders' and move to 'My Orders Page'"""
        self.UserIconClick()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable
                                             ((By.CSS_SELECTOR,
                                               "#loginMiniTitle > label[translate='My_Orders']")))
        self.driver.find_element_by_css_selector("#loginMiniTitle > label[translate='My_Orders']").click()

    def GetOrdersNum(self):
        """Return list of order number"""
        self.SeeMyorders()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located \
                                                 ((By.CSS_SELECTOR, ".cover > table > tbody")))
        orders=[]
        table = self.driver.find_element_by_css_selector(".cover > table > tbody")
        rows = table.find_elements_by_css_selector("tr.ng-scope ")
        for row in rows:
            cells = row.find_elements_by_tag_name("td")
            order_num = cells[0].find_element_by_class_name("ng-binding").text
            orders.append(order_num)
        return orders

    def SignOut(self):
        """LogOut From account"""
        sleep(2)
        self.UserIconClick()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable
                                             ((By.CSS_SELECTOR,"label[ng-click='signOut($event)']")))
        self.driver.find_element_by_css_selector("label[ng-click='signOut($event)']").click()


    def Account_In_Out(self):
        """Return account is in the system or not"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located
                                             ((By.CSS_SELECTOR, "#menuUserLink>span")))
        username= self.driver.find_element_by_css_selector("#menuUserLink>span")
        if username.is_displayed():
            return "The account signed in"
        else:
            return "The account signed out"

