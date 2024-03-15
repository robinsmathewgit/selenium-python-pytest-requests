import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('common info', 'base_url')
        return url

    @staticmethod
    def get_test_data_file():
        test_data_file = config.get('common info', 'test_data_file')
        return test_data_file

    @staticmethod
    def get_web_element_timeout():
        timeout = config.get('common info', 'timeout_web_element')
        return timeout

    @staticmethod
    def get_screenshot_folder():
        screenshot_folder = config.get('common info', 'screenshot_folder')
        return screenshot_folder

    @staticmethod
    def get_selenium_grid_url():
        grid_url = config.get('common info', 'selenium_grid')
        return grid_url

    @staticmethod
    def get_api_payload_folder():
        payload_folder = config.get('api info', 'api_payload')
        return payload_folder

    @staticmethod
    def get_api_base_uri():
        base_uri = config.get('api info', 'api_base_uri')
        return base_uri
