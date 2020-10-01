from AOS_Selenium.Page_Objects.Page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisteredUser(Page):
    """This class holds headers page functions that unique for registered user"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def see_my_orders(self):
        """Click on 'My Orders' and move to 'My Orders Page'"""
        self.user_icon_click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable
                                             ((By.CSS_SELECTOR,
                                               "#loginMiniTitle > label[translate='My_Orders']")))
        self.driver.find_element_by_css_selector("#loginMiniTitle > label[translate='My_Orders']").click()

    def get_orders_num(self):
        """Return list of order number"""
        self.see_my_orders()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located \
                                                 ((By.CSS_SELECTOR, ".cover > table > tbody")))
        orders = []
        table = self.driver.find_element_by_css_selector(".cover > table > tbody")
        rows = table.find_elements_by_css_selector("tr.ng-scope ")
        for row in rows:
            cells = row.find_elements_by_tag_name("td")
            order_num = cells[0].find_element_by_class_name("ng-binding").text
            orders.append(order_num)
        return orders

    def sign_out(self):
        """LogOut From account"""
        self.user_icon_click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable
                                             ((By.CSS_SELECTOR, "label[ng-click='signOut($event)']")))
        self.driver.find_element_by_css_selector("label[ng-click='signOut($event)']").click()
