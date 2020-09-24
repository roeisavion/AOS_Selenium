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

    def test_login_logout(self):
        """This test check if account can to sign in/out"""

        """Check login"""
        self.guest.sign_in()
        self.assertTrue(self.guest.account_in_out() == "The account signed in")

        """Check logout"""
        self.registered.sign_out()
        self.assertTrue(self.registered.account_in_out() == "The account signed out")






