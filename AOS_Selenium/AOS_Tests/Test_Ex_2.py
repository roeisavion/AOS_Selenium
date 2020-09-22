from selenium import webdriver
from AOS_Selenium.Page_Objects.Main_AOS import MainPage
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
        self.AOS.ClickCategory("Speakers")
        self.speakers.ClickProduct(1)
        self.product1.Add_Product_To_Cart(2)
        self.product1_details = self.product1.GetProductDetails()
        self.product1.BackToMainPage()

        """#3: Add Product 2 to Cart"""
        self.AOS.ClickCategory("Laptops")
        self.laptops.ClickProduct(1)
        self.product2.Add_Product_To_Cart(3)
        self.product2_details = self.product2.GetProductDetails()
        self.product2.BackToMainPage()


        """#4: Add Product 3 to Cart"""
        self.AOS.ClickCategory("Tablets")
        self.tablets.ClickProduct(1)
        self.product3.Add_Product_To_Cart(5)
        self.product3_details = self.product3.GetProductDetails()


    def tearDown(self):
        print("TearDown")
    def test_cart_details(self):
        """This test will check if the details of each product are correct"""
        Cart_Details = self.product3.GetCartDetails()
        print(Cart_Details)

        """Product one check"""
        print(Cart_Details[3])
        print(self.product1_details)
        self.assertIn(Cart_Details[3], self.product1_details)

        """Product two check"""
        print(self.product2_details)
        print(Cart_Details[2])
        self.assertIn(Cart_Details[2], self.product2_details)

        """Product three check"""
        print(self.product3_details)
        print(Cart_Details[1])
        self.assertIn(Cart_Details[1], self.product3_details)

















