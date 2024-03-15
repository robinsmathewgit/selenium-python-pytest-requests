import pytest
import requests
from utilities.custom_logger import Log, Logger
from utilities.read_properties import ReadConfig
from tests_api.api_end_points import apiEndPoints


class TestProductPurchase:
    logger = Logger.init()

    # Submit a GET request to https://jsonplaceholder.typicode.com/users/1
    # Check that the response status code is equal to 200
    def test_get_user_with_id_1_check_status_code_equals_200(self):
        url = ReadConfig.get_api_base_uri() + apiEndPoints.get('get_user') + '/1'
        Log.message(f"Test Condition: Submit a GET request to {url}", self.logger)
        Log.message("Expected Result: Response status code is equal to 200", self.logger)
        response = requests.get(url, verify=False)
        Log.message(f"Actual Result: Response status code is {response.status_code}", self.logger)
        assert response.status_code == 200, 'Status code is not as expected'

    # Submit a GET request to https://jsonplaceholder.typicode.com/users/1
    # Check that the response header 'Content-Type' is equal to 'application/json; charset=utf-8'
    def test_get_user_with_id_1_check_content_type_equals_json(self):
        url = ReadConfig.get_api_base_uri() + apiEndPoints.get('get_user') + '/1'
        Log.message(f"Test Condition: Submit a GET request to {url}", self.logger)
        Log.message("Expected Result: Response header 'Content-Type' is equal to 'application/json; charset=utf-8'",
                    self.logger)
        response = requests.get(url, verify=False)
        Log.message(f"Actual Result: Response header 'Content-Type' is {response.headers['Content-Type']}", self.logger)
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8', 'Content-Type is not as expected'

    # Submit a GET request to https://jsonplaceholder.typicode.com/users/1
    # Check that the response body field 'name' exists
    def test_get_user_with_id_1_check_name_field_exists(self):
        url = ReadConfig.get_api_base_uri() + apiEndPoints.get('get_user') + '/1'
        Log.message(f"Test Condition: Submit a GET request to {url}", self.logger)
        Log.message("Expected Result: Response body field 'name' exists", self.logger)
        response = requests.get(url, verify=False)
        response_body = response.json()
        Log.message(f"Actual Result: Response body field 'name' exists {'name' in response_body}", self.logger)
        assert 'name' in response_body, 'Name field doesnt exist in the response body'

    # Submit a GET request to https://jsonplaceholder.typicode.com/users/1
    # Check that the response body field 'name' has a value equal to 'Leanne Graham'
    def test_get_user_with_id_1_check_name_equals_leanne_graham(self):
        url = ReadConfig.get_api_base_uri() + apiEndPoints.get('get_user') + '/1'
        Log.message(f"Test Condition: Submit a GET request to {url}", self.logger)
        Log.message("Expected Result: Response body field 'name' has a value equal to 'Leanne Graham'", self.logger)
        response = requests.get(url, verify=False)
        response_body = response.json()
        Log.message(f"Actual Result: Response body field 'name' has a value equal to {response_body['name']}",
                    self.logger)
        assert response_body['name'] == 'Leanne Graham', 'Name in the body is not displayed as expected'

    # Submit a GET request to https://jsonplaceholder.typicode.com/users/1
    # Check that the response body field 'company.name' has a value equal to 'Romaguera-Crona'
    def test_get_user_with_id_1_check_company_name_equals_romaguera_crona(self):
        url = ReadConfig.get_api_base_uri() + apiEndPoints.get('get_user') + '/1'
        Log.message(f"Test Condition: Submit a GET request to {url}", self.logger)
        Log.message("Expected Result: Response body field 'company.name' has a value equal to 'Romaguera-Crona'",
                    self.logger)
        response = requests.get(url, verify=False)
        response_body = response.json()
        Log.message(f"Actual Result: Response body field 'company.name' has a value equal to "
                    f"{response_body['company']['name']}",
                    self.logger)
        assert response_body['company']['name'] == 'Romaguera-Crona', \
            'Company Name in the body is not displayed as expected'

    # Submit a GET request to https://jsonplaceholder.typicode.com/users
    # Check that the response body is a list (an array) containing 10 elements
    def test_get_all_users_check_number_of_users_equals_10(self):
        url = ReadConfig.get_api_base_uri() + apiEndPoints.get('get_user')
        Log.message(f"Test Condition: Submit a GET request to {url}", self.logger)
        Log.message("Expected Result: Response body is a list (an array) containing 10 elements", self.logger)
        response = requests.get(url, verify=False)
        response_body = response.json()
        Log.message("Actual Result: Response body is a list (an array) containing 10 elements", self.logger)
        assert len(response_body) == 10, 'response body doesnt containing 10 elements'

    # Submit a POST request to https://jsonplaceholder.typicode.com/posts
    # to create a new post with a title, body and associated user ID (1-10)
    # Check that the response status code equals HTTP 201 (Created)
    def test_post_new_post_check_status_code_equals_201(self):
        url = ReadConfig.get_api_base_uri() + apiEndPoints.get('post_user')
        Log.message(f"Test Condition: Submit a POST request to {url}", self.logger)
        Log.message("Expected Result: Response status code equals 201", self.logger)
        post_data = {"userId": 1,
                     "title": "My post title",
                     "body": "My post body"}
        response = requests.post(url, json=post_data, verify=False)
        Log.message(f"Actual Result: Response status code is {response.status_code}", self.logger)
        assert response.status_code == 201, 'Status code is not as expected'

    test_data_users = [(1, "Leanne Graham"), (2, "Ervin Howell"), (3, "Clementine Bauch")]

    # Submit a GET request to retrieve user data for the specified user IDs
    # Check that the response body field 'name' is equal to the specified expected name
    @pytest.mark.parametrize('userid, expected_name', test_data_users)
    def test_get_data_for_user_check_name(self, userid, expected_name):
        url = ReadConfig.get_api_base_uri() + apiEndPoints.get('get_user') + '/' + str(userid)
        Log.message("Test Condition: Submit a GET request to retrieve user data for the specified user IDs", self.logger)
        Log.message(f"Expected Result: Response body field 'name' is equal to {expected_name}", self.logger)
        response = requests.get(url, verify=False)
        response_body = response.json()
        Log.message(f"Actual Result: Response body field 'name' is equal to {response_body['name']}", self.logger)
        assert response_body['name'] == expected_name, 'Name in the body is not displayed as expected'
