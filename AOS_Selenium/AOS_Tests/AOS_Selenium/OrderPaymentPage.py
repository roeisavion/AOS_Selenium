from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AOS_Selenium.Page import Page

class OrderPaymentPage(Page) :
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def Click_Register(self):
        self.driver.find_element_by_id("registration_btnundefined").click()

    def Enter_Login_Username(self,username):
        self.driver.find_element_by_name("usernameInOrderPayment").send_keys(username)

    def Enter_Login_Password(self,password):
        self.driver.find_element_by_name("passwordInOrderPayment").send_keys(password)

    def Click_Login(self):
        self.driver.find_element_by_id("login_btnundefined").click()

    def Click_Next(self):
        self.driver.find_element_by_id("next_btn").click()

    def Click_Edit_shipping_details(self):
        self.driver.find_element_by_css_selector('.ng-scope[translate="Edit_shipping_Details"]').click()

    def Choose_SafePay(self):
        # WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.NAME,"safepay")))
        self.driver.find_element_by_name("safepay").click()

    def Choose_MasterCredit(self):
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "MasterCredit")))
        self.driver.find_element_by_css_selector('img[alt="Master credit"]').click()

    def Enter_SafePay_Username(self,username):
        self.driver.find_element_by_name("safepay_username").send_keys(username)

    def Enter_SafePay_Password(self,password):
        self.driver.find_element_by_name("safepay_password").send_keys(password)

    def Click_Pay_Now_SafePay(self):
        self.driver.find_element_by_id("pay_now_btn_SAFEPAY").click()




    def Enter_CardHolder_name(self,cardholdername):
        # self.driver.find_element_by_name("cardholder_name").click()
        self.driver.find_element_by_name("cardholder_name").send_keys(cardholdername)

    def Enter_CrditCard_number(self,CrditCard_number):
        # self.driver.find_element_by_name("card_number").click()
        self.driver.find_element_by_name("card_number").send_keys(CrditCard_number)

    def Enter_CVV_number(self,CVV_number):
        # self.driver.find_element_by_name("cvv_number").click()
        self.driver.find_element_by_name("cvv_number").send_keys(CVV_number)

    def Click_MM(self):
        self.driver.find_element_by_name("mmListbox").click()

    def Choose_MM(self,mm):
        self.driver.find_element_by_css_selector(f'.ng-pristine[name="mmListbox"]>option[label="{mm}"]').click()

    def Click_YYYY(self):
        self.driver.find_element_by_name("yyyyListbox").click()

    def Choose_YYYY(self,yyyy):
        self.driver.find_element_by_css_selector(f'.ng-pristine[name="yyyyListbox"]>option[label="{yyyy}"]').click()

    def Enter_Exp_Date(self,mm,yyyy):
        self.Click_MM()
        self.Choose_MM(mm)
        self.Click_YYYY()
        self.Choose_YYYY(yyyy)

    def Pay_Now_MasterCredit_after_details(self):
        #WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "pay_now_btn_ManualPayment")))
        self.driver.find_element_by_id("pay_now_btn_ManualPayment").click()

    def Pay_Now_MasterCredit_with_saved_details(self):
        self.driver.find_element_by_id("pay_now_btn_MasterCredit").click()

    def Edit_MasterCredit_Details(self):
            self.driver.find_element_by_css_selector('label[translate="Edit"]').click()

    def Check_Thank_you(self):
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"span[translate='Thank_you_for_buying_with_Advantage']"),'Thank you for buying with Advantage'))
        return self.driver.find_element_by_css_selector("span[translate='Thank_you_for_buying_with_Advantage']").text

    def GetOrderNumber(self):
        return self.driver.find_element_by_id("orderNumberLabel").text