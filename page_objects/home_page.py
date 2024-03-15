from selenium.webdriver.common.by import By

from utilities.read_properties import ReadConfig


class HomePage:
    css_btn_women_tab = "a[title='Women']"

    def __init__(self, driver):
        self.driver = driver
        self.timeout = int(ReadConfig.get_web_element_timeout())

    def click_summer_dress_from_women(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_btn_women_tab).click()
