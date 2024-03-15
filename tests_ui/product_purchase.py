import pytest

from page_objects.home_page import HomePage
from page_objects.product_page import ProductPage
from utilities.custom_logger import Log, Logger
from utilities.read_properties import ReadConfig


class TestProductPurchase:
    base_url = ReadConfig.get_application_url()
    logger = Logger.init()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_product_purchase_test_one(self, setup):
        Log.message("Testcase: test_product_purchase", self.logger)
        self.driver = setup
        self.driver.get(self.base_url)
        Log.message("Verifying Product Page Title", self.logger)
        Log.message_screenshot("Testcase: test_product_purchase", self.logger, self.driver)
        self.homePage = HomePage(self.driver)
        self.homePage.click_summer_dress_from_women()
        self.productPage = ProductPage(self.driver)
        self.is_loaded = self.productPage.is_summer_dress_page_loaded()

        if self.is_loaded:
            self.driver.close()
            Log.pass_test("Test Result: Test Passed", self.logger)
        else:
            self.driver.close()
            Log.fail_test("Test Result: Test Failed", self.logger, self.driver)

    @pytest.mark.regression
    def test_product_purchase_test_two(self, setup):
        Log.message("Testcase: test_product_purchase", self.logger)
        self.driver = setup
        self.driver.get(self.base_url)
        Log.message("Verifying Product Page Title", self.logger)
        Log.message_screenshot("Testcase: test_product_purchase", self.logger, self.driver)
        self.homePage = HomePage(self.driver)
        self.homePage.click_summer_dress_from_women()
        self.productPage = ProductPage(self.driver)
        self.is_loaded = self.productPage.is_summer_dress_page_loaded()

        if self.is_loaded:
            self.driver.close()
            Log.pass_test("Test Result: Test Passed", self.logger)
        else:
            self.driver.close()
            Log.fail_test("Test Result: Test Failed", self.logger, self.driver)
