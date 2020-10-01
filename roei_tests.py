from selenium import webdriver
from AOS_Selenium.Page_Objects.MainPage import MainPage
from AOS_Selenium.Page_Objects.CategoryPage import CategoryPage
from AOS_Selenium.Page_Objects.ProductPage import ProductPage
from AOS_Selenium.Page_Objects.GuestUser import GuestUser
from AOS_Selenium.Page_Objects.RegisteredUser import RegisteredUser
from AOS_Selenium.Page_Objects.OrderPaymentPage import OrderPaymentPage
from AOS_Selenium.Page_Objects.ShoppingCartPage import ShoppingCartPage
from AOS_Selenium.Page_Objects.Creat_Account import CreateAccount
from unittest import TestCase
from time import sleep


class TestQA(TestCase):
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
        self.shopping_cart_page = ShoppingCartPage(self.driver)
        self.order_payment = OrderPaymentPage(self.driver)
        self.create_account_page = CreateAccount(self.driver)

    def tearDown(self):
        self.driver.quit()
        print("TearDown")

    def test4_going_to_cart_page(self):
        """This test will check if page navigate to cart page"""

        """Add Product 1 to Cart"""
        self.AOS.click_category("Speakers")
        self.speakers.click_product(number_in_page=5)
        self.product1.add_product_to_cart(quantity=2)
        self.product1.back_to_main_page()

        """Add Product 2 to Cart"""
        self.AOS.click_category("Laptops")
        self.laptops.click_product(number_in_page=6)
        self.product2.add_product_to_cart(quantity=3)

        """navigate to cart page"""
        self.product1.cart_click()
        self.assertIn(self.shopping_cart_page.check_navigation_line(), 'SHOPPING CART')
        print(self.shopping_cart_page.check_navigation_line())

    def test5_print_cart(self):
        """This test will check if cart details are correct"""

        """Add Product 1 to Cart"""
        self.AOS.click_category("Speakers")
        self.speakers.click_product(number_in_page=5)
        self.product1.add_product_to_cart(quantity=2)
        self.product1.back_to_main_page()

        """Add Product 2 to Cart"""
        self.AOS.click_category("Laptops")
        self.laptops.click_product(number_in_page=6)
        self.product2.add_product_to_cart(quantity=3)
        self.product2.back_to_main_page()

        """Add Product 3 to Cart"""
        self.AOS.click_category("Tablets")
        self.tablets.click_product(number_in_page=3)
        self.product3.add_product_to_cart(quantity=4)

        """Navigate to cart page"""
        self.product3.cart_click()
        self.shopping_cart_page.cart_print()
        self.assertEqual(self.shopping_cart_page.sum_cart_prices(), self.shopping_cart_page.get_checkout_price())

    def test6_edit_quantity(self):
        """This test will check if edit products"""

        """Add Product 1 to Cart"""
        self.AOS.click_category("Speakers")
        self.speakers.click_product(number_in_page=5)
        self.product1.add_product_to_cart(quantity=2)
        self.product1.back_to_main_page()

        """Add Product 2 to Cart"""
        self.AOS.click_category("Laptops")
        self.laptops.click_product(number_in_page=6)
        self.product2.add_product_to_cart(quantity=3)

        """Navigate to cart page"""
        self.product2.cart_click()
        sleep(2)

        """Edit products quantity"""
        self.shopping_cart_page.edit_quantity(1, 5)
        self.shopping_cart_page.edit_quantity(2, 6)

        self.shopping_cart_page.cart_details()
        self.assertEqual(int(self.shopping_cart_page.products_quantity[0].text), 6)
        self.assertEqual(int(self.shopping_cart_page.products_quantity[1].text), 5)

    def test8_new_user_paying_SafePay(self):
        """This test will check a payment with safepay"""
        """Add Product 1 to Cart"""
        self.AOS.click_category("Speakers")
        self.speakers.click_product(number_in_page=5)
        self.product1.add_product_to_cart(quantity=2)
        self.product1.back_to_main_page()

        """Add Product 2 to Cart"""
        self.AOS.click_category("Laptops")
        self.laptops.click_product(number_in_page=6)
        self.product2.add_product_to_cart(quantity=3)
        self.product2.back_to_main_page()

        """Add Product 3 to Cart"""
        self.AOS.click_category("Tablets")
        self.tablets.click_product(number_in_page=3)
        self.product3.add_product_to_cart(quantity=4)

        """Navigate to cart page"""
        self.product3.cart_click()

        """Payment with safepay"""
        self.AOS.click_check_out()
        self.order_payment.click_register()
        self.create_account_page.register_account()
        sleep(2)
        self.order_payment.click_next()
        self.order_payment.choose_safepay()
        self.order_payment.enter_safepay_username('abcd1234')
        self.order_payment.enter_safepay_password('Abcd12345')
        self.order_payment.click_pay_now_safepay()
        # sleep(3)
        print(self.order_payment.check_thank_you())
        # sleep(2)

        """Check if the payment was successful"""
        self.assertEqual('Thank you for buying with Advantage', self.order_payment.check_thank_you())

        """check if the order is shown in "my orders"""
        order_number = self.order_payment.get_order_number()
        last_order = self.registered.get_last_order_num()
        print(order_number)
        print(last_order)
        self.assertTrue(last_order == order_number)

        """check if the cart is empty"""
        self.order_payment.back_to_main_page()
        self.assertTrue(self.AOS.find_cart_is_empty())

    def test9_existing_user_paying_credit_card(self):
        """This test will check a payment with master credit"""
        """Add Product 1 to Cart"""
        self.AOS.click_category("Speakers")
        self.speakers.click_product(number_in_page=5)
        self.product1.add_product_to_cart(quantity=2)
        self.product1.back_to_main_page()

        """Add Product 2 to Cart"""
        self.AOS.click_category("Laptops")
        self.laptops.click_product(number_in_page=6)
        self.product2.add_product_to_cart(quantity=3)
        self.product2.back_to_main_page()

        """Add Product 3 to Cart"""
        self.AOS.click_category("Tablets")
        self.tablets.click_product(number_in_page=3)
        self.product3.add_product_to_cart(quantity=4)

        """Navigate to cart page"""
        self.product3.cart_click()

        """Payment with master credit"""
        self.AOS.click_check_out()
        self.order_payment.login()
        self.order_payment.click_next()
        self.order_payment.choose_master_credit()

        try:
            self.order_payment.enter_credit_card_number('4886567890123456')
            self.order_payment.enter_cvv_number('7744')
            self.order_payment.enter_cardholder_name('abcde')
            self.order_payment.enter_exp_date('03', '2026')
            self.order_payment.pay_now_master_credit_after_details()
        except:
            # self.op.Edit_MasterCredit_Details()
            self.order_payment.pay_now_master_credit_with_saved_details()

        """Check if the payment was successful"""
        self.assertEqual('Thank you for buying with Advantage', self.order_payment.check_thank_you())

        """check if the order is shown in "my orders"""
        order_number = self.order_payment.get_order_number()
        last_order = self.registered.get_last_order_num()
        print(order_number)
        print(last_order)
        self.assertTrue(last_order == order_number)


        """check if the cart is empty"""
        self.order_payment.back_to_main_page()
        self.assertTrue(self.AOS.find_cart_is_empty())
