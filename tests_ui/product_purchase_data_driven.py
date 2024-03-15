import pytest

from page_objects.home_page import HomePage
from page_objects.product_page import ProductPage
from utilities import xl_utils
from utilities.custom_logger import Log, Logger
from utilities.read_properties import ReadConfig


class TestProductPurchaseDataDriven:
    base_url = ReadConfig.get_application_url()
    test_data_file = ReadConfig.get_test_data_file()

    logger = Logger.init()

    @pytest.mark.regression
    def test_product_purchase_test_data_driven_one(self):
        Log.message("Testcase: test_product_purchase", self.logger)
        Log.message("Verifying Product Page Title", self.logger)

        self.dataCellValue = xl_utils.get_data(self.test_data_file, 'Test_Data_Sheet_1', 'TC_003', 'Data')
        Log.message("Data Value - " + str(self.dataCellValue), self.logger)

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_product_purchase_test_data_driven_two(self, setup):
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