from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidSelectorException
from Page_Objects.Page import Page
from selenium.webdriver.common.action_chains import ActionChains


class ProductPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.productNames=[]
        self.productQuantities=[]
        self.productPrices=[]

# Product Page Functions
    def set_quantity(self, quantity):
        """Set quantity of product"""
        self.driver.find_element_by_css_selector(f"input[numbers-only='""']").click()
        self.driver.find_element_by_css_selector("input[numbers-only='""']").send_keys(str(quantity))

    def click_add_to_cart(self):
        """Click 'Add To Cart' button"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located \
                                                 ((By.CSS_SELECTOR, "button[translate='ADD_TO_CART']")))
        self.driver.find_element_by_css_selector("button[translate='ADD_TO_CART']").click()

    def add_product_to_cart(self, quantity):
        """Adding Product to cart"""
        if quantity < 1 or quantity > 10 or type(quantity) != int:
            quantity = 1
        self.set_quantity(quantity)
        self.click_add_to_cart()

# Product Details functions
    def get_name(self):
        """Return product name"""
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element((By.CSS_SELECTOR, "ul>li>tool-tip-cart>div>table")))    #wait for cart menu to disappear
        return self.driver.find_element_by_css_selector("h1[class='roboto-regular screen768 ng-binding']").text

    def get_price(self):
        """Return product price"""
        price = self.driver.find_element_by_xpath(
            "//div[@id='Description']/h2[@class='roboto-thin screen768 ng-binding']").text
        price = price.replace('$','')
        price = price.replace(',','')
        return price

    def get_quantity(self):
        """Returns the quantity I set on a product page"""
        quantity = self.driver.find_element_by_css_selector("input[numbers-only='""']").get_attribute("value")
        return quantity

    def get_selected_color(self):
        """Returns the color I set on a product page"""
        try:
            color = self.driver.find_element_by_css_selector("span#rabbit.colorSelected")
        except InvalidSelectorException:
            color = self.driver.find_element_by_css_selector("span#bunny.colorSelected")
        return color.get_attribute("title")

    def get_product_details(self):
        """Returns the product details I selected, the color, and the quantity"""
        name = self.get_name()
        color = self.get_selected_color()
        qty = self.get_quantity()
        price = self.get_price()

        product_details = f'Name= {name}, Color= {color}, Quantity= {int(qty)}, Price= {(float(price)) * (int(qty))}'
        return product_details

    def add_product_details_to_list(self):
        """saves the name, quantity and price of a product from the product page in lists"""
        name = self.get_name()
        self.productNames.insert(0,name)
        quantity = self.get_quantity()
        self.productQuantities.insert(0,quantity)
        price = self.get_price()
        self.productPrices.insert(0, price)
