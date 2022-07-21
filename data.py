import secrets


class Data:

    @staticmethod
    def random_string():
        return f'{secrets.token_hex()}'

    def get_random_user_data(self):
        data = {
            "id": 11,
            "name": f"Test {self.random_string()}",
            "username": f"Test.{self.random_string()}",
            "email": f"Test.{self.random_string()}@test.com",
            "address": {
                "street": "Test Street",
                "suite": "Suite 100",
                "city": f"{self.random_string()}",
                "zipcode": "11101",
                "geo": {
                    "lat": "-39.2386",
                    "lng": "58.2232"
                }
            },
            "phone": "024-648-3800",
            "website": f"{self.random_string()}.com",
            "company": {
                "name": f"name-{self.random_string()}",
                "catchPhrase": f"{self.random_string()}",
                "bs": f"{self.random_string()}"
            }
        }
        return data
