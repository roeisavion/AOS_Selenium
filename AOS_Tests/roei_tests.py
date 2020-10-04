from selenium import webdriver
from Page_Objects.MainPage import MainPage
from Page_Objects.CategoryPage import CategoryPage
from Page_Objects.ProductPage import ProductPage
from Page_Objects.GuestUser import GuestUser
from Page_Objects.RegisteredUser import RegisteredUser
from Page_Objects.OrderPaymentPage import OrderPaymentPage
from Page_Objects.ShoppingCartPage import ShoppingCartPage
from Page_Objects.Creat_Account import CreateAccount
from time import sleep
from unittest import TestCase


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
        self.categoryPage = CategoryPage(self.driver)
        self.productPage = ProductPage(self.driver)
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
        self.categoryPage.click_product(number_in_page=5)
        self.productPage.add_product_to_cart(quantity=2)
        self.productPage.back_to_main_page()


        """Add Product 2 to Cart"""
        self.AOS.click_category("Laptops")
        self.categoryPage.click_product(number_in_page=6)
        self.productPage.add_product_to_cart(quantity=3)


        """Navigate to cart page"""
        self.productPage.cart_click()
        self.assertIn(self.shopping_cart_page.check_navigation_line(), 'SHOPPING CART')
        print(self.shopping_cart_page.check_navigation_line())

    def test5_print_cart(self):
        """This test will check if cart details are correct"""


        """Add Product 1 to Cart"""
        self.AOS.click_category("Speakers")
        self.categoryPage.click_product(number_in_page=5)
        self.productPage.add_product_to_cart(quantity=2)

        self.productPage.add_product_details_to_list()
        self.productPage.back_to_main_page()

        """Add Product 2 to Cart"""
        self.AOS.click_category("Laptops")
        self.categoryPage.click_product(number_in_page=6)
        self.productPage.add_product_to_cart(quantity=3)

        self.productPage.add_product_details_to_list()
        self.productPage.back_to_main_page()

        """Add Product 3 to Cart"""
        self.AOS.click_category("Tablets")
        self.categoryPage.click_product(number_in_page=3)
        self.productPage.add_product_to_cart(quantity=4)

        self.productPage.add_product_details_to_list()

        """Navigate to cart page"""
        self.productPage.cart_click()
        self.shopping_cart_page.cart_print()

        '''checks details on shopping cart page match details from the ordered product page'''
        for i in range(len(self.productPage.productNames)) :
            self.assertEqual(self.productPage.productNames[i],self.shopping_cart_page.product_names[i].text)
            self.assertEqual(self.productPage.productQuantities[i],self.shopping_cart_page.products_quantity[i].text)

            self.shopping_cart_page.products_price[i]=self.shopping_cart_page.products_price[i].text.replace(',','').replace('$','')
            productPage_price=float(self.productPage.productPrices[i])*int(self.productPage.productQuantities[i])
            self.assertEqual(productPage_price,float(self.shopping_cart_page.products_price[i]))

        '''checks is the checkout price equals the sum of the prices(from the shopping cart page) in the cart'''
        self.assertEqual(self.shopping_cart_page.sum_cart_prices(), self.shopping_cart_page.get_checkout_price())


    def test6_edit_quantity(self):
        """This test will check if edit products"""

        """Add Product 1 to Cart"""
        self.AOS.click_category("Speakers")
        self.categoryPage.click_product(number_in_page=5)
        self.productPage.add_product_to_cart(quantity=2)
        self.productPage.back_to_main_page()


        """Add Product 2 to Cart"""
        self.AOS.click_category("Laptops")
        self.categoryPage.click_product(number_in_page=6)
        self.productPage.add_product_to_cart(quantity=3)

        """Navigate to cart page"""
        self.productPage.cart_click()

        """Edit products quantity"""
        self.shopping_cart_page.edit_quantity(0, 5)
        self.shopping_cart_page.edit_quantity(1, 6)

        self.shopping_cart_page.cart_details()
        self.assertEqual(int(self.shopping_cart_page.products_quantity[0].text), 5)
        self.assertEqual(int(self.shopping_cart_page.products_quantity[1].text), 6)

    def test8_new_user_paying_SafePay(self):
        """This test will check a payment with safepay"""
        """Add Product 1 to Cart"""
        self.AOS.click_category("Speakers")
        self.categoryPage.click_product(number_in_page=5)
        self.productPage.add_product_to_cart(quantity=2)
        self.productPage.back_to_main_page()

        """Add Product 2 to Cart"""
        self.AOS.click_category("Laptops")
        self.categoryPage.click_product(number_in_page=6)
        self.productPage.add_product_to_cart(quantity=3)
        self.productPage.back_to_main_page()

        """Add Product 3 to Cart"""
        self.AOS.click_category("Tablets")
        self.categoryPage.click_product(number_in_page=3)
        self.productPage.add_product_to_cart(quantity=4)

        """Navigate to cart page"""
        self.productPage.cart_click()

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

        print(self.order_payment.check_thank_you())


        """Check if the payment was successful"""
        self.assertEqual('Thank you for buying with Advantage', self.order_payment.check_thank_you())

        """check if the order is shown in "my orders"""
        order_number = self.order_payment.get_order_number()
        last_order = self.registered.get_orders_num()
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
        self.categoryPage.click_product(number_in_page=5)
        self.productPage.add_product_to_cart(quantity=2)
        self.productPage.back_to_main_page()

        """Add Product 2 to Cart"""
        self.AOS.click_category("Laptops")
        self.categoryPage.click_product(number_in_page=6)
        self.productPage.add_product_to_cart(quantity=3)
        self.productPage.back_to_main_page()

        """Add Product 3 to Cart"""
        self.AOS.click_category("Tablets")
        self.categoryPage.click_product(number_in_page=3)
        self.productPage.add_product_to_cart(quantity=4)

        """Navigate to cart page"""
        self.productPage.cart_click()

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
        last_order = self.registered.get_orders_num()
        print(order_number)
        print(last_order)
        self.assertTrue(last_order == order_number)


        """check if the cart is empty"""
        self.order_payment.back_to_main_page()
        self.assertTrue(self.AOS.find_cart_is_empty())


