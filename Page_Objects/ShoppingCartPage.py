from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AOS_Selenium.Page_Objects.ProductPage import ProductPage
from AOS_Selenium.Page_Objects.Page import Page


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
        return self.table

    def cart_details(self):
        self.cart_table()
        self.product_names = self.table.find_elements_by_css_selector(".productName")
        self.products_quantity = self.table.find_elements_by_css_selector('.quantityMobile>label.ng-binding')
        self.products_price = self.table.find_elements_by_css_selector("tbody>tr>td>p")

    def cart_print(self):
        self.cart_details()
        for i in range(len(self.product_names)):
            print(f'{self.product_names[i].text}  {self.products_quantity[i].text}  {self.products_price[i].text}')

    def sum_cart_prices(self):
        self.cart_details()

        self.sum_prices=0
        for i in range(len(self.product_names)):
            self.sum_prices += float(self.products_price[i].text.replace(",", '').replace("$", ''))

        self.sum_prices = round(self.sum_prices, 2)
        return self.sum_prices

    def get_checkout_price(self):
        self.checkout_price = self.table.find_element_by_css_selector(
            '.fixedTableEdgeCompatibility > tfoot:nth-child(3) > tr > td[colspan="2"] > span:nth-child(2)')

        self.checkout_price = float(self.checkout_price.text.replace(",", '').replace("$", ''))
        return self.checkout_price

    def edit_quantity(self,product_num_in_table,new_quantity):
        self.cart_table()
        edits= self.table.find_elements_by_css_selector('a[translate="EDIT"]')
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element((By.CSS_SELECTOR,"ul>li>tool-tip-cart>div>table")))
        edits[product_num_in_table-1].click()
        pp1=ProductPage(self.driver)
        pp1.set_quantity(new_quantity)
        pp1.click_add_to_cart()