import unittest
import requests
import json
from data import Data


REQUEST_URL = "https://jsonplaceholder.typicode.com/users"


class UsersTest(unittest.TestCase):
    def setUp(self):
        data_set = Data()
        self.data = data_set.get_random_user_data()
        self.json_data = open('parameters.json', 'r')
        self.test_data = json.load(self.json_data)

    def tearDown(self):
        self.json_data.close()

    def test_get_users_request(self):  # TC1
        response = requests.get(url=REQUEST_URL)
        self.assertTrue(response.status_code == 200)
        json_response = json.loads(response.text)
        self.assertTrue(len(json_response) == 10)

    def test_get_users_request_id(self):  # TC2
        expected_id = self.test_data[0]["expected_id"]
        expected_name = self.test_data[0]["expected_name"]
        response = requests.get(url=REQUEST_URL)
        self.assertTrue(response.status_code == 200)
        json_response = json.loads(response.text)
        for user in json_response:
            if user["id"] == expected_id:
                self.assertTrue(user["name"] == expected_name)

    def test_post_users_request(self):  # TC3
        response = requests.post(url=REQUEST_URL, json=self.data)
        self.assertTrue(response.status_code == 201)
        json_response = json.loads(response.text)
        self.assertTrue(json_response == self.data)


if __name__ == '__main__':
    unittest.main()
