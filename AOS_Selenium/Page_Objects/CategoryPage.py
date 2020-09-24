from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AOS_Selenium.Page_Objects.Page import Page


class CategoryPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def total_products(self):
        """Return the quantity of products in category page"""
        element_total = self.driver.find_element_by_class_name("titleItemsCount")
        total = int(element_total.text[0:1])
        return total

    def product_in_list(self, number_in_page):
        """Find products element"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located \
                                                 ((By.CSS_SELECTOR, f"div.cell>ul>li.ng-scope:nth-child({number_in_page})")))
        return self.driver.find_element_by_css_selector(f"div.cell>ul>li.ng-scope:nth-child({number_in_page})")

    def click_product(self, number_in_page):
        """Click on product"""
        if number_in_page < 1 or number_in_page > self.total_products() or type(number_in_page) != int:
            number_in_page = 1
        self.product_in_list(number_in_page).click()

    def find_title(self):
        """Return the title of category page"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located \
                                                 ((By.CLASS_NAME, "categoryTitle")))
        title = self.driver.find_element_by_class_name("categoryTitle")
        return title.text
