import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from helpers.api_helper import UserApi

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(
        options=chrome_options
    )
    yield driver
    driver.quit()

@pytest.fixture
def authorized_user():
    api = UserApi()
    user_data, response = api.register_new_user()
    access_token = response.json().get('accessToken')
    yield {
        'credentials': user_data,
        'token': access_token
    }
    if access_token:
        api.delete_user(access_token)
