from selenium import webdriver
from AOS_Selenium.Page_Objects.MainPage import MainPage
from AOS_Selenium.Page_Objects.CategoryPage import CategoryPage
from AOS_Selenium.Page_Objects.ProductPage import ProductPage
from AOS_Selenium.Page_Objects.GuestUser import GuestUser
from AOS_Selenium.Page_Objects.RegisteredUser import RegisteredUser
from unittest import TestCase


class TestQuantity(TestCase):
    def setUp(self):
        print("SetUp")
        self.driver = webdriver.Chrome \
            (executable_path=r"C:\Users\Student\Desktop\Selenium\chromedriver.exe")
        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        """SetUp Objects"""
        self.AOS = MainPage(self.driver)
        self.speakers = CategoryPage(self.driver)
        self.laptops = CategoryPage(self.driver)
        self.tablets = CategoryPage(self.driver)
        self.product1 = ProductPage(self.driver)
        self.product2 = ProductPage(self.driver)
        self.product3 = ProductPage(self.driver)
        self.guest = GuestUser(self.driver)
        self.registered = RegisteredUser(self.driver)

    def tearDown(self):
        print("TearDown")

    def test_set_quantity(self):
        """This test will check if the quantity of cart items is correct"""

        """Add Product 1 to Cart"""
        self.AOS.click_category("Speakers")
        self.speakers.click_product(number_in_page=5)
        self.product1.add_product_to_cart(quantity=2)
        qty_prod_1 = self.product1.get_product_quantity_from_cart()
        self.product1.back_to_main_page()
        print(qty_prod_1)

        """Add Product 2 to Cart"""
        self.AOS.click_category("Laptops")
        self.laptops.click_product(number_in_page=6)
        self.product2.add_product_to_cart(quantity=3)
        qty_prod_2 = self.product2.get_product_quantity_from_cart()
        self.product2.back_to_main_page()
        print(qty_prod_2)

        """Add Product 3 to Cart"""
        self.AOS.click_category("Tablets")
        self.tablets.click_product(number_in_page=3)
        self.product3.add_product_to_cart(quantity=4)
        qty_prod_3 = self.product3.get_product_quantity_from_cart()
        print(qty_prod_3)

        """Get cart total quantity"""
        cart_quantity = self.product1.cart_total_quantity()

        """Sum of products quantities"""
        sum_products = qty_prod_1 + qty_prod_2 + qty_prod_3

        """Check if sum of products quantities are equal to Cart Quantity"""
        self.assertEqual(cart_quantity, sum_products)
        print(cart_quantity, sum_products)
        self.product3.back_to_main_page()
        self.driver.quit()

