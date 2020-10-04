from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Objects.ProductPage import ProductPage
from Page_Objects.Page import Page
from selenium.webdriver.common.action_chains import ActionChains




class ShoppingCartPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_navigation_line(self):
        """Check if navigate to shopping cart page"""
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"select"),'SHOPPING CART'))
        return self.driver.find_element_by_class_name("select").text

    def cart_table(self):
        self.table=self.driver.find_element_by_css_selector("table.fixedTableEdgeCompatibility")

    def cart_details(self):
        '''rerurns 3 lists of elements of the products names,quantities and prices from the shopping cart page '''
        self.cart_table()
        self.product_names = self.table.find_elements_by_css_selector(".productName")
        self.products_quantity = self.table.find_elements_by_css_selector('.quantityMobile>label.ng-binding')
        self.products_price = self.table.find_elements_by_css_selector("tbody>tr>td>p")

        for i in range(len(self.product_names)):
            self.product_names[i]=self.product_names[i].text
            self.products_quantity[i]=int(self.products_quantity[i].text)
            self.products_price[i]=float(self.products_price[i].text.replace(',','').replace('$',''))

        return self.product_names,self.products_quantity,self.products_price

    def cart_print(self):
        '''prints the cart details'''
        self.cart_details()
        for i in range(len(self.product_names)):
            print(f'product name:{self.product_names[i]}  quantity:{self.products_quantity[i]}  price:{self.products_price[i]}')

    def sum_cart_prices(self):
        '''sums up the prices from the cart and returns it'''
        self.cart_details()
        self.sum_prices=0
        for i in range(len(self.product_names)):
            self.sum_prices += self.products_price[i]

        self.sum_prices = round(self.sum_prices, 2)
        return self.sum_prices

    def get_checkout_price(self):
        '''returns the checkout price as a float number '''
        self.checkout_price = self.table.find_element_by_css_selector(
            '.fixedTableEdgeCompatibility > tfoot:nth-child(3) > tr > td[colspan="2"] > span:nth-child(2)')
        self.checkout_price = float(self.checkout_price.text.replace(",", '').replace("$", ''))
        return self.checkout_price

    def edit_quantity(self,product_num_in_table,new_quantity):
        self.cart_table()

        '''moving mouse away from icon until the dropDown menu disappear'''
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector('h3.sticky')).perform()
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element((By.CSS_SELECTOR,"ul>li>tool-tip-cart>div>table")))

        edits = self.table.find_elements_by_css_selector('a[translate="EDIT"]')
        edits[product_num_in_table].click()
        pp1=ProductPage(self.driver)
        pp1.set_quantity(new_quantity)
        pp1.click_add_to_cart()