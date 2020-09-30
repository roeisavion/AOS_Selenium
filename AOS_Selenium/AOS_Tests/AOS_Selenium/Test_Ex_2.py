from selenium import webdriver
from time import sleep
from AOS_Selenium.Main_AOS import MainPage
from AOS_Selenium.CategoryPage import CategoryPage
from AOS_Selenium.ProductPage import Product
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

        self.Category = CategoryPage(self.driver)

        self.Product = Product(self.driver)

        self.Product = Product(self.driver)

        """#2: Add Product 1 to Cart"""
        self.AOS.ClickCategory("Speakers")

        self.Category.ClickProduct("Speakers", 1)

        self.Product.Set_Quantity(3)

        self.Product.Click_Add_To_Cart()

        self.Product_1_Details = self.Product.GetProductDetails()

        self.driver.back()
        self.driver.back()

        """#3: Add Product 2 to Cart"""
        self.AOS.ClickCategory("Laptops")

        self.Category.ClickProduct("Laptops", 1)

        self.Product.Set_Quantity(2)

        self.Product.Click_Add_To_Cart()

        self.Product_2_Details = self.Product.GetProductDetails()

        self.driver.back()
        self.driver.back()

        """#4: Add Product 3 to Cart"""
        self.AOS.ClickCategory("Headphones")

        self.Category.ClickProduct("Headphones", 1)

        self.Product.Set_Quantity(5)

        self.Product.Click_Add_To_Cart()

        self.Product_3_Details = self.Product.GetProductDetails()

    def tearDown(self):
        print("TearDown")
    def test_cart_details(self):
        """This test will check if the details of each product are correct"""
        Cart_Details = self.Product.GetCartDetails()
        print(Cart_Details)

        """Product one check"""
        print(self.Product_1_Details)
        print(Cart_Details[3])
        self.assertTrue(Cart_Details[3] == self.Product_1_Details)

        """Product two check"""
        print(self.Product_3_Details)
        print(Cart_Details[1])
        self.assertTrue(Cart_Details[1] == self.Product_3_Details)

        """Product three check"""
        print(self.Product_2_Details)
        print(Cart_Details[2])
        self.assertTrue(Cart_Details[2] == self.Product_2_Details)

















