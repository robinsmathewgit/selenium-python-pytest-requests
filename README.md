# Python-PyTest-Requests(UI/API) Automation Framework

This project is a test automation framework built using Python, pytest, and the Requests library. It includes UI tests, API tests, and reporting using Allure.

## Project Structure

- **configurations**: Contains configuration files for the project, stored as `config.ini`.
- **page_objects**: Page Objects for UI test suites are stored in this folder.
- **reports**: Allure reports will be generated in this folder.
- **test_data**: Test data for the automation suites are stored in this folder.
- **tests_ui**: UI tests are located in this folder.
- **tests_api**: API tests are stored in this folder.
- **utilities**: Reusable/utility classes are stored in this folder.

## Setup

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Ensure configurations are set up properly in the `config.ini` file.
4. Ensure test data is available in the `test_data` folder.
5. Run UI tests using `pytest tests_ui`.
6. Run API tests using `pytest tests_api`.
7. Allure reports will be generated in the `reports` folder after test execution.

## Dependencies

- Python
- pytest
- Requests library
- Allure

## Usage

1. To run UI tests:

```bash
pytest tests_ui
```
2. To run APII tests:

```bash
pytest tests_api
```
