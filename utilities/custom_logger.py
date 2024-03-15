import logging
import os
import threading
from random import randint

import allure
from allure_commons.types import AttachmentType

# Creating lock for threads
lock = threading.Lock()


def get_screenshot_name():
    full_name = os.environ.get('PYTEST_CURRENT_TEST').split(' ')[0]
    test_name = full_name.split("::")[1]
    return test_name + '_' + str(randint(0, 100)) + ".png"


class Logger:

    logger = None

    @staticmethod
    def init():
        lock.acquire()
        if Logger.logger is None:

            # Create Logger
            Logger.logger = logging.getLogger(__name__)
            Logger.logger.setLevel(logging.INFO)

            # Create console handler or file handler and set Log level
            ch = logging.StreamHandler()
            fh = logging.FileHandler(".\\logs\\automation.log")

            # Create formatter
            formatter = logging.Formatter('%(message)s:')

            # Add formatter to console or file handler
            ch.setFormatter(formatter)
            fh.setFormatter(formatter)

            # Add console handler to logger
            Logger.logger.addHandler(ch)
            Logger.logger.addHandler(fh)
            lock.release()
        return Logger.logger


class Log:

    @staticmethod
    def message(message, logger):
        logger.info(message)

    @staticmethod
    def message_screenshot(message, logger, driver):
        screenshot_name = get_screenshot_name()
        logger.info(message + ' - ' + screenshot_name)
        allure.attach(driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=AttachmentType.PNG)

    @staticmethod
    def pass_test(message, logger):
        logger.info(message)
        assert True

    @staticmethod
    def fail_test(message, logger, driver):
        screenshot_name = get_screenshot_name()
        allure.attach(driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=AttachmentType.PNG)
        logger.error(message + ' - ' + screenshot_name)
        assert False
