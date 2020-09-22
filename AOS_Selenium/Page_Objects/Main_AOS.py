from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AOS_Selenium.Page_Objects.Page import Page
from time import sleep

class MainPage(Page):

    Categoties_id = {"Tablets": 'tabletsImg', "Laptops": 'laptopsImg', "Mice": 'miceImg', "Headphones": 'headphonesImg',
                     "Speakers": 'speakersImg'}

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def FindCategory(self, category):
        """Find category element"""
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element
                                             ((By.CSS_SELECTOR, ".loader:nth-child(2)")))
        return self.driver.find_element_by_id(MainPage.Categoties_id[category])

    def ClickCategory(self, category):
        """Click on category"""
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable\
                                                  ((By.ID, MainPage.Categoties_id[category])))
        self.FindCategory(category).click()

