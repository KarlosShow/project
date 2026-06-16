import requests
from helpers.user_generator import UserGenerator
from data.urls import REGISTER_USER_URL
from data.urls import DELETE_USER_URL

class UserApi:
    def __init__(self):
        self.session = requests.Session()
    def register_new_user(self):
        credentials = UserGenerator.create_credentials()
        response = self.session.post(
            REGISTER_USER_URL,
            json=credentials,
            timeout=15
        )
        return credentials, response
    def delete_user(self, token):
        headers = {
            'Authorization': token
        }
        return self.session.delete(
            DELETE_USER_URL,
            headers=headers,
            timeout=15
        )
