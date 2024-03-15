import json

import requests

from utilities.custom_logger import Log, Logger
from utilities.read_properties import ReadConfig
from tests_api.api_end_points import apiEndPoints


class TestProductPurchaseCrud:
    logger = Logger.init()

    # Submit a POST request to https://jsonplaceholder.typicode.com/posts
    # to create a new post with a title, body and associated user ID (1-10)
    # Check that the response status code equals HTTP 201 (Created)
    def test_curd_post_new_post_check_status_code_equals_201(self):
        url = ReadConfig.get_api_base_uri() + apiEndPoints.get('post_user')
        Log.message(f"Test Condition: Submit a POST request to {url}", self.logger)
        Log.message("Expected Result: Response status code equals 201", self.logger)
        post_data = open(ReadConfig.get_api_payload_folder() + 'first_post.json', 'r').read()
        response = requests.post(url, data=json.loads(post_data), verify=False)
        Log.message(f"Actual Result: Response status code is {response.status_code}", self.logger)
        assert response.status_code == 201, 'Status code is not as expected'
