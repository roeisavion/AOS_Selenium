from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from time import sleep


class Page:
    """Class 'Page' holds simple functions for page"""

    def __init__(self, driver):
        self.driver = driver

    def back_to_main_page(self):
        """This func navigate to 'Main page', by click on main page icon"""
        self.driver.find_element_by_css_selector("a[ng-click='go_up()']").click()

    # Icon Cart Functions
    def find_cart(self):
        """Find 'Cart' icon element"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located \
                                                 ((By.ID, "menuCart")))
        return self.driver.find_element_by_id("menuCart")

    def mouse_on_icon_cart(self):
        """Put mouse on 'Cart' icon"""
        cart = self.find_cart()
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(cart).perform()

    def cart_click(self):
        """CLick on 'Cart' icon"""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable \
                                                 ((By.ID, "menuCart")))
        self.find_cart().click()

    def cart_total_quantity(self):
        """Return total of 'Cart' items"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located \
                                                 ((By.XPATH, "//label[@class='roboto-regular ng-binding']")))
        text = self.driver.find_element_by_xpath("//label[@class='roboto-regular ng-binding']").text
        end_num_index = text.index(' ')
        quantity = int(text[1:end_num_index])
        return quantity

    def get_product_quantity_from_cart(self, index=0):
        """Return specific product quantity in cart"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located \
                                                 ((By.XPATH, "//label[contains(text(), 'QTY')]")))
        quantities = self.driver.find_elements_by_xpath("//label[contains(text(), 'QTY')] ")
        if index < 0 or type(index) != int:
            index = 0
        elif index > len(quantities - 1):
            index = len(quantities - 1)
        qty_of_prod = int(quantities[index].text[5:])
        return qty_of_prod

    def get_cart_details(self):
        """Return dictionary of the products and their: name, color, quantity, price"""
        table = self.driver.find_element_by_tag_name('tbody')
        rows = table.find_elements_by_tag_name('tr')
        products = {}
        i = 1
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located \
                                                 ((By.TAG_NAME, "tbody")))
        for row in rows:
            name = row.find_element_by_css_selector('td>a>h3').text
            qty = row.find_element_by_css_selector('td>a>label').text
            color = row.find_element_by_css_selector('td>a>label>span').text
            price = row.find_element_by_css_selector('td>p').text
            for char in price:
                if char == ',':
                    price = price.replace(char, '')
            for char2 in name:
                if char2 == '.':
                    name = name.replace(char2, '')
            products[i] = f'Name= {name} ,Color= {color},Quantity= {int(qty[5:])},Price= {price[1:]}'
            i += 1
        return products

    def remove_product_from_cart(self):
        """Remove one product from cart"""
        removes = self.driver.find_elements_by_css_selector('.removeProduct')
        removes[0].click()

    # CheckOut simple functions
    def find_check_out(self):
        """Return CheckOut button element"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located \
                                                 ((By.ID, "checkOutPopUp")))
        return self.driver.find_element_by_id("checkOutPopUp")

    def click_check_out(self):
        """Clicking CheckOut button"""
        self.find_check_out().click()

    def find_cart_is_empty(self):
        self.mouse_on_icon_cart()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located \
                                                 ((By.CSS_SELECTOR, "div.emptyCart")))
        return self.driver.find_element_by_css_selector("div.emptyCart").text

    # User simple functions
    def user_icon_click(self):
        """Click on user icon"""
        sleep(2)
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element
                                             ((By.CSS_SELECTOR, ".loader:nth-child(1)")))
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element
                                             ((By.CSS_SELECTOR, ".loader:nth-child(2)")))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable
                                             ((By.CSS_SELECTOR, "#menuUser")))
        user_icon = self.driver.find_element_by_css_selector("#menuUser")
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(user_icon)
        user_icon.click()

    def account_in_out(self):
        """Return account is in the system or not"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located
                                             ((By.CSS_SELECTOR, "#menuUserLink")))
        username = self.driver.find_element_by_css_selector("#menuUserLink>span")
        if username.is_displayed():
            return "The account signed in"
        else:
            return "The account signed out"
