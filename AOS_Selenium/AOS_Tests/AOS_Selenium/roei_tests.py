from selenium import webdriver
from time import sleep
from AOS_Selenium.Main_AOS import MainPage
from AOS_Selenium.CategoryPage import CategoryPage
from AOS_Selenium.OrderPaymentPage import OrderPaymentPage
from AOS_Selenium.CrateAccountPage import CreateAccountPage
from AOS_Selenium.MyOrderPage import MyOrdersPage
from AOS_Selenium.ProductPage import ProductPage
from AOS_Selenium.Page import Page
from unittest import TestCase
from AOS_Selenium.ShoppingCartPage import *


class Tests(TestCase):
    def setUp(self):
        print("SetUp")
        driver = webdriver.Chrome(executable_path=r'C:\Users\Saba\Desktop\QA\WebDrivers\chromedriver.exe')
        driver.get("http://www.advantageonlineshopping.com/#/")
        driver.implicitly_wait(10)
        driver.maximize_window()

        self.pp=ProductPage(driver)
        self.cp=CategoryPage(driver)
        self.mp=MainPage(driver)
        self.driver=driver
        self.scp=ShoppingCartPage(driver)
        self.op=OrderPaymentPage(driver)
        self.cap=CreateAccountPage(driver)
        self.mo=MyOrdersPage(driver)





    def test4_going_to_cart_page(self):
        self.mp.ClickCategory("Speakers")

        self.cp.add_product_to_cart_category_page(1,"BLACK",3)
        self.cp.add_product_to_cart_category_page(1, "GRAY", 4)
        self.cp.add_product_to_cart_category_page(2, "RED", 2)

        self.cp.CartClick()
        self.assertIn(self.scp.check_navigation_line(),'SHOPPING CART')
        print(self.scp.check_navigation_line())

    def test5_print_cart(self):
        self.mp.ClickCategory("Speakers")

        self.cp.add_product_to_cart_category_page(1,"BLACK",3)
        self.cp.add_product_to_cart_category_page(1, "GRAY", 4)
        self.cp.add_product_to_cart_category_page(2, "RED", 2)
        self.cp.CartClick()

        self.scp.cart_print()
        self.assertEqual(self.scp.sum_cart_prices(), self.scp.get_checkout_price())

    def test6_edit_quantity(self):

        self.mp.ClickCategory("Speakers")

        self.cp.add_product_to_cart_category_page(1,"BLACK",3)
        self.cp.add_product_to_cart_category_page(1, "GRAY", 4)
        self.cp.add_product_to_cart_category_page(2, "RED", 2)
        self.cp.CartClick()
        sleep(2)
        self.scp.edit_quantity(1,5)
        self.scp.edit_quantity(2,6)

        self.scp.cart_details()
        self.assertEqual(int(self.scp.products_quantity[0].text),5)
        self.assertEqual(int(self.scp.products_quantity[1].text),6)


    def test8_new_user_paying_SafePay(self):

        self.mp.ClickCategory("Speakers")

        self.cp.add_product_to_cart_category_page(1,"BLACK",3)
        self.cp.add_product_to_cart_category_page(1, "GRAY", 4)
        self.cp.add_product_to_cart_category_page(2, "RED", 2)

        self.mp.ClickOnCheckout()
        self.op.Click_Register()
        self.cap.Account_Username("Trying01")
        self.cap.Account_Password("Abcd1234")
        self.cap.Confirm_Password("Abcd1234")
        self.cap.Account_Email("abcd6@gmail.com")
        sleep(2)
        self.cap.Click_I_Aggree()
        sleep(2)
        self.cap.Click_Register()
        # sleep(2)
        self.op.Click_Next()
        self.op.Choose_SafePay()
        self.op.Enter_SafePay_Username('abcd1234')
        self.op.Enter_SafePay_Password('Abcd12345')
        self.op.Click_Pay_Now_SafePay()
        # sleep(3)
        print(self.op.Check_Thank_you())
        # sleep(2)

        # check if the payment was successful
        self.assertEqual('Thank you for buying with Advantage',self.op.Check_Thank_you())

        order_number=self.op.GetOrderNumber()

        #check if the cart is empty
        self.assertTrue(self.op.CheckEmptyCart())

        #check if the order is shown in "my orders"
        self.op.MyOrdersClick()
        self.assertEqual(self.mo.GetLastOrderNumber(),order_number)
        print(order_number)


    def test9_existing_user_paying_CreditCard(self):

        self.mp.ClickCategory("Speakers")

        self.cp.add_product_to_cart_category_page(1,"BLACK",3)
        self.cp.add_product_to_cart_category_page(1, "GRAY", 4)
        self.cp.add_product_to_cart_category_page(2, "RED", 2)

        self.cp.ClickOnCheckout()

        self.op.Enter_Login_Username("Trying01")
        self.op.Enter_Login_Password("Abcd1234")
        self.op.Click_Login()
        self.op.Click_Next()

        self.op.Choose_MasterCredit()
        try :
            self.op.Enter_CrditCard_number('4886567890123456')
            self.op.Enter_CVV_number('7744')
            self.op.Enter_CardHolder_name('abcde')
            self.op.Enter_Exp_Date('03','2026')
            self.op.Pay_Now_MasterCredit_after_details()
        except:
            # self.op.Edit_MasterCredit_Details()
            self.op.Pay_Now_MasterCredit_with_saved_details()


        # check if the payment was successful
        self.assertEqual('Thank you for buying with Advantage', self.op.Check_Thank_you())

        order_number = self.op.GetOrderNumber()

        # check if the cart is empty
        self.assertTrue(self.op.CheckEmptyCart())

        # check if the order is shown in "my orders"
        self.op.MyOrdersClick()
        self.assertEqual(self.mo.GetLastOrderNumber(), order_number)
        print(order_number)














