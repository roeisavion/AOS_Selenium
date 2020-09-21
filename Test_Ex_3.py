from selenium import webdriver
from time import sleep
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

    def test_RemoveProductFromCart(self):
        """This test will check if removed product are still in cart """
        Cart_Details= self.product3.GetCartDetails()
        print(Cart_Details)

        product3_details = Cart_Details[1]
        print(product3_details)

        self.product3.RemoveProductFromCart()

        Cart_Details1 = self.product3.GetCartDetails()
        print(Cart_Details1)

        self.assertNotIn(product3_details,Cart_Details1)





