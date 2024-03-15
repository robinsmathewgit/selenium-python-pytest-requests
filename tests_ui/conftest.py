import pytest

from selenium import webdriver
from utilities.read_properties import ReadConfig


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Remote(
            command_executor=ReadConfig.get_selenium_grid_url(),
            options=chrome_options
        )
    elif browser == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        driver = webdriver.Remote(
            command_executor=ReadConfig.get_selenium_grid_url(),
            options=firefox_options
        )
    else:
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Remote(
            command_executor=ReadConfig.get_selenium_grid_url(),
            options=chrome_options
        )
    driver.maximize_window()
    return driver


def pytest_addoption(parser):  # This is to get the value from CLI
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return Browser value to set up method
    return request.config.getoption("--browser")


#  Pytest HTML report
#  This is a hook for adding Environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Product Purchase Application POC'
    config._metadata['Module Name'] = 'Product Purchase'


#  This is a hook for Delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
