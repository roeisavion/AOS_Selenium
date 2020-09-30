from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AOS_Selenium.Page import Page


class MainPage(Page):

    Categoties_id = {"Tablets": 'tabletsImg', "Laptops": 'laptopsImg', "Mice": 'miceImg', "Headphones": 'headphonesImg',
                     "Speakers": 'speakersImg'}

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def FindCategory(self, category):
        """Find category element"""
        self.driver.find_element_by_id(MainPage.Categoties_id[category])

    def ClickCategory(self, category):
        """Click on category"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located \
                                                  ((By.ID, MainPage.Categoties_id[category])))

        self.driver.find_element_by_id(MainPage.Categoties_id[category]).click()
