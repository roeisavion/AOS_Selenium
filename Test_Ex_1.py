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

    def test_set_quantity(self):
        """This test will check if the quantity of cart items is correct"""
        Cart_Quantity = self.product1.CartTotalQuantity()

        """Sum of products quantities"""
        Sum_Products = self.product1.GetProductQuantityFromCart(0) + self.product2.GetProductQuantityFromCart(1)+ self.product3.GetProductQuantityFromCart(2)

        """Check if sum of products quantities are equal to Cart Quantity"""
        self.assertEqual(Cart_Quantity, Sum_Products)
        print(Cart_Quantity, Sum_Products)
