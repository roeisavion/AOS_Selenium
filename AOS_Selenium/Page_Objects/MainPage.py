from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AOS_Selenium.Page_Objects.Page import Page


class MainPage(Page):
    Categoties_id = {"Tablets": 'tabletsImg', "Laptops": 'laptopsImg', "Mice": 'miceImg', "Headphones": 'headphonesImg',
                     "Speakers": 'speakersImg'}

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def find_category(self, category):
        """Find category element"""
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element
                                             ((By.CSS_SELECTOR, ".loader:nth-child(2)")))
        return self.driver.find_element_by_id(MainPage.Categoties_id[category])

    def click_category(self, category):
        """Click on category"""
        if category not in MainPage.Categoties_id:
            category = "Tablets"
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable \
                                                 ((By.ID, MainPage.Categoties_id[category])))
        self.find_category(category).click()

    def location(self):
        """This function will help us to check if we are in main page"""
        element = self.driver.find_element_by_css_selector("#special_offer_items>h3")
        if element.is_displayed():
            return "MainPage"
        else:
            return "Not in MainPage"
