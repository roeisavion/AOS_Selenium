from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Objects.Page import Page
from selenium.webdriver.support.select import Select


class OrderPaymentPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_register(self):
        self.driver.find_element_by_id("registration_btnundefined").click()

    def enter_login_username(self,username):
        self.driver.find_element_by_name("usernameInOrderPayment").send_keys(username)

    def enter_login_password(self, password):
        self.driver.find_element_by_name("passwordInOrderPayment").send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id("login_btnundefined").click()

    def login(self):
        self.enter_login_username("maor90b8989")
        self.enter_login_password("12345aA")
        self.click_login()

    def click_next(self):
        self.driver.find_element_by_id("next_btn").click()

    def click_edit_shipping_details(self):
        self.driver.find_element_by_css_selector('.ng-scope[translate="Edit_shipping_Details"]').click()

    def choose_safepay(self):
        # WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.NAME,"safepay")))
        self.driver.find_element_by_name("safepay").click()

    def choose_master_credit(self):
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "MasterCredit")))
        self.driver.find_element_by_css_selector('img[alt="Master credit"]').click()

    def enter_safepay_username(self,username):
        self.driver.find_element_by_name("safepay_username").send_keys(username)

    def enter_safepay_password(self,password):
        self.driver.find_element_by_name("safepay_password").send_keys(password)

    def click_pay_now_safepay(self):
        self.driver.find_element_by_id("pay_now_btn_SAFEPAY").click()

    def enter_cardholder_name(self,card_holder_name):
        # self.driver.find_element_by_name("cardholder_name").click()
        self.driver.find_element_by_name("cardholder_name").send_keys(card_holder_name)

    def enter_credit_card_number(self,credit_card_number):
        # self.driver.find_element_by_name("card_number").click()
        self.driver.find_element_by_name("card_number").send_keys(credit_card_number)

    def enter_cvv_number(self,cvv_number):
        # self.driver.find_element_by_name("cvv_number").click()
        self.driver.find_element_by_name("cvv_number").send_keys(cvv_number)

    def click_mm(self):
        self.driver.find_element_by_name("mmListbox").click()

    def choose_mm(self,mm):
        select = Select(self.driver.find_element_by_name('mmListbox'))
        select.select_by_visible_text(mm)

    def click_yyyy(self):
        self.driver.find_element_by_name("yyyyListbox").click()

    def choose_yyyy(self,yyyy):
        select = Select(self.driver.find_element_by_name('yyyyListbox'))
        select.select_by_visible_text(yyyy)

    def enter_exp_date(self, mm, yyyy):
        self.choose_mm(mm)
        self.choose_yyyy(yyyy)

    def pay_now_master_credit_after_details(self):
        #WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "pay_now_btn_ManualPayment")))
        self.driver.find_element_by_id("pay_now_btn_ManualPayment").click()

    def pay_now_master_credit_with_saved_details(self):
        self.driver.find_element_by_id("pay_now_btn_MasterCredit").click()

    def edit_master_credit_details(self):
        self.driver.find_element_by_css_selector('label[translate="Edit"]').click()

    def check_thank_you(self):
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"span[translate='Thank_you_for_buying_with_Advantage']"),'Thank you for buying with Advantage'))
        return self.driver.find_element_by_css_selector("span[translate='Thank_you_for_buying_with_Advantage']").text

    def get_order_number(self):
        return self.driver.find_element_by_id("orderNumberLabel").text
