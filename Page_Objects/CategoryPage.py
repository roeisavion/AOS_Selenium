from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Objects.Page import Page
from random import randint

class CategoryPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def total_products(self):
        """Return the quantity of products in category page"""
        element_total = self.driver.find_element_by_class_name("titleItemsCount")
        text = element_total.text
        end_num_index = text.index(' ')
        total = int(text[0: end_num_index])
        return total

    def product_in_list(self, number_in_page):
        """Find products element"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located \
                                                 ((By.CSS_SELECTOR, f"div.cell>ul>li.ng-scope:nth-child({number_in_page})")))
        return self.driver.find_element_by_css_selector(f"div.cell>ul>li.ng-scope:nth-child({number_in_page})")

    def click_product(self, number_in_page):
        """Click on product"""

    def click_product(self, number_in_page=1):
        """Click on product"""
        total = self.total_products()
        if number_in_page < 1 or number_in_page > total or type(number_in_page) != int or number_in_page is None:
            number_in_page = randint(1, total)
        # Check if product soldout
        sold_out_element = self.product_in_list(number_in_page).find_element_by_css_selector("div.soulOut")
        while sold_out_element.is_displayed():
            number_in_page = randint(1, total)
        self.product_in_list(number_in_page).click()

    def find_title(self):
        """Return the title of category page"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located \
                                                 ((By.CLASS_NAME, "categoryTitle")))
        title = self.driver.find_element_by_class_name("categoryTitle")
        return title.text
