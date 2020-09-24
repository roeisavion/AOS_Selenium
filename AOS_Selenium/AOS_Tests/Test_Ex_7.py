from selenium import webdriver
from AOS_Selenium.Page_Objects.MainPage import MainPage
from AOS_Selenium.Page_Objects.CategoryPage import CategoryPage
from AOS_Selenium.Page_Objects.ProductPage import ProductPage
from unittest import TestCase
from AOS_Selenium.Page_Objects.GuestUser import GuestUser
from AOS_Selenium.Page_Objects.RegisteredUser import RegisteredUser

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
        self.guest = GuestUser(self.driver)
        self.registered = RegisteredUser(self.driver)

    def tearDown(self):
        print("TearDown")

    def test_navigate_back(self):
        """Add tablet to Cart"""
        self.AOS.click_category("Tablets")
        self.tablets.click_product(number_in_page=3)
        self.product3.add_product_to_cart(quantity=4)

        """check if navigate tablet page"""
        self.driver.back()
        self.assertTrue(self.tablets.find_title() == "TABLETS")

        """check if navigate to main page"""
        self.driver.back()
        element = self.AOS.find_special_offer()
        self.assertTrue("SPECIAL OFFER" == element.text)




