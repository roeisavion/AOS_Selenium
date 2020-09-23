from selenium import webdriver
from AOS_Selenium.Page_Objects.MainPage import MainPage
from AOS_Selenium.Page_Objects.CategoryPage import CategoryPage
from AOS_Selenium.Page_Objects.ProductPage import ProductPage
from unittest import TestCase


class TestQuantity(TestCase):
    def setUp(self):
        print("SetUp")
        self.driver = webdriver.Chrome \
            (executable_path=r"C:\Users\Student\Desktop\Selenium\chromedriver.exe")
        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        """#1 : SetUp Objects"""
        self.AOS = MainPage(self.driver)
        self.speakers = CategoryPage(self.driver)
        self.laptops = CategoryPage(self.driver)
        self.tablets = CategoryPage(self.driver)
        self.product1 = ProductPage(self.driver)
        self.product2 = ProductPage(self.driver)
        self.product3 = ProductPage(self.driver)

        """#2: Add Product 1 to Cart"""
        self.AOS.click_category("Speakers")
        self.speakers.click_product(1)
        self.product1.add_product_to_cart(2)
        self.product1_details = self.product1.get_product_details()
        self.product1.back_to_main_page()

        """#3: Add Product 2 to Cart"""
        self.AOS.click_category("Laptops")
        self.laptops.click_product(1)
        self.product2.add_product_to_cart(3)
        self.product2_details = self.product2.get_product_details()
        self.product2.back_to_main_page()

        """#4: Add Product 3 to Cart"""
        self.AOS.click_category("Tablets")
        self.tablets.click_product(1)
        self.product3.add_product_to_cart(5)
        self.product3_details = self.product3.get_product_details()

    def tearDown(self):
        print("TearDown")

    def test_cart_details(self):
        """This test will check if the details of each product are correct"""
        cart_details = self.product3.get_cart_details()
        print(cart_details)

        """Product one check"""
        print(cart_details[3])
        print(self.product1_details)
        self.assertIn(cart_details[3], self.product1_details)

        """Product two check"""
        print(self.product2_details)
        print(cart_details[2])
        self.assertIn(cart_details[2], self.product2_details)

        """Product three check"""
        print(self.product3_details)
        print(cart_details[1])
        self.assertIn(cart_details[1], self.product3_details)

















