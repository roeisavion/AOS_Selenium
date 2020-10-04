from selenium import webdriver
from Page_Objects.MainPage import MainPage
from Page_Objects.CategoryPage import CategoryPage
from Page_Objects.ProductPage import ProductPage
from Page_Objects.GuestUser import GuestUser
from Page_Objects.RegisteredUser import RegisteredUser
from unittest import TestCase
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestQA(TestCase):
    def setUp(self):
        print("SetUp")
        self.driver = webdriver.Chrome \
            (executable_path=r'C:\Users\Saba\Desktop\QA\WebDrivers\chromedriver.exe')
        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        """SetUp Objects"""
        self.AOS = MainPage(self.driver)
        self.category = CategoryPage(self.driver)
        self.product = ProductPage(self.driver)
        self.guest = GuestUser(self.driver)
        self.registered = RegisteredUser(self.driver)

    def tearDown(self):
        self.driver.quit()
        print("TearDown")

    def test_set_quantity(self):  # Ex 1
        """This test will check if the quantity of cart items is correct"""

        """Add Product 1 to Cart"""
        self.AOS.click_category("Speakers")
        self.category.click_product(number_in_page=5)
        self.product.add_product_to_cart(quantity=2)
        qty_prod_1 = self.product.get_product_quantity_from_cart()
        self.product.back_to_main_page()
        print('product1 quantity = ',qty_prod_1)

        """Add Product 2 to Cart"""
        self.AOS.click_category("Laptops")
        self.category.click_product(number_in_page=6)
        self.product.add_product_to_cart(quantity=3)
        qty_prod_2 = self.product.get_product_quantity_from_cart()
        self.product.back_to_main_page()
        print('product2 quantity = ',qty_prod_2)

        """Add Product 3 to Cart"""
        self.AOS.click_category("Tablets")
        self.category.click_product(number_in_page=3)
        self.product.add_product_to_cart(quantity=4)
        qty_prod_3 = self.product.get_product_quantity_from_cart()
        print('product3 quantity = ',qty_prod_3)

        """Get cart total quantity"""
        cart_quantity = self.product.cart_total_quantity()

        """Sum of products quantities"""
        sum_products = qty_prod_1 + qty_prod_2 + qty_prod_3

        """Check if sum of products quantities are equal to Cart Quantity"""
        self.assertEqual(cart_quantity, sum_products)
        print('sum cart quantity =', cart_quantity)
        print('sum products quantity =', sum_products)
        self.product.back_to_main_page()

    def test_cart_details(self):  # Ex 2
        """This test will check if the details of each product in the cart are correct"""

        """Add Product 1 to Cart"""
        self.AOS.click_category("Speakers")
        self.category.click_product(number_in_page=5)
        self.product.add_product_to_cart(quantity=2)
        self.product1_details = self.product.get_product_details()
        self.product.back_to_main_page()

        """Add Product 2 to Cart"""
        self.AOS.click_category("Laptops")
        self.category.click_product(number_in_page=6)
        self.product.add_product_to_cart(quantity=3)
        self.product2_details = self.product.get_product_details()
        self.product.back_to_main_page()

        """Add Product 3 to Cart"""
        self.AOS.click_category("Tablets")
        self.category.click_product(number_in_page=3)
        self.product.add_product_to_cart(quantity=4)
        self.product3_details = self.product.get_product_details()

        """Get all products cart details """
        cart_details = self.product.get_cart_details()
        print("cart details =",cart_details)

        """Product one check"""
        print("product 1 in cart =",cart_details[3])
        print("product 1 in product page =",self.product1_details)
        self.assertIn(self.product1_details, cart_details[3])

        """Product two check"""
        print("product 2 in product page =",self.product2_details)
        print("product 2 in cart =",cart_details[2])
        self.assertIn(self.product2_details, cart_details[2])

        """Product three check"""
        print("product 3 in product page =",self.product3_details)
        print("product 3 in cart =",cart_details[1])
        self.assertIn(self.product3_details, cart_details[1])
        self.product.back_to_main_page()

    def test_RemoveProductFromCart(self):  # Ex 3
        """This test will check if removed product are still in cart """

        """Add Product 1 to Cart"""
        self.AOS.click_category("Speakers")
        self.category.click_product(number_in_page=5)
        self.product.add_product_to_cart(quantity=2)
        self.product1_details = self.product.get_product_details()
        print("product 1 in product page =",self.product1_details)
        self.product.back_to_main_page()

        """Add Product 2 to Cart"""
        self.AOS.click_category("Laptops")
        self.category.click_product(number_in_page=6)
        self.product.add_product_to_cart(quantity=3)
        self.product2_details = self.product.get_product_details()
        print("product 2 in product page =",self.product2_details)

        """Get products cart details"""
        cart_details = self.product.get_cart_details()
        print("cart details =",cart_details)

        """Get product2 details from cart details """
        product2_details = cart_details[1]
        print("product 2 in cart =",product2_details)

        """Remove product2"""
        self.product.remove_product_from_cart()

        """Get products cart details after removing product2"""
        cart_details_after_remove = self.product.get_cart_details()
        print("cart after remove =",cart_details_after_remove)
        self.assertNotIn(product2_details, cart_details_after_remove)
        self.product.back_to_main_page()

    def test_navigate_back(self):  # Ex 7
        """Add tablet to Cart"""
        self.AOS.click_category("Tablets")
        self.category.click_product(number_in_page=3)
        self.product.add_product_to_cart(quantity=4)

        """check if navigate tablet page"""
        self.driver.back()
        self.assertTrue(self.category.find_title() == "TABLETS")

        """check if navigate to main page"""
        self.driver.back()
        location = self.AOS.location()
        self.assertTrue(location == "MainPage")

    def test_login_logout(self):  # Ex 10
        """This test check if account is able to sign in/out"""

        """Check login"""
        self.guest.sign_in()
        self.assertTrue(self.guest.account_in_out() == 'The account signed in')

        """Check logout"""
        self.registered.sign_out()
        self.assertTrue(self.registered.account_in_out() == 'The account signed out')


