import base_client
from datetime import datetime
debug = True


class ClientGetID(base_client.BaseClient):
    method = "users"
    # GET, POST, ...
    http_method = "get"

    def __init__(self, username):
        self.username = username
        self.json_data = None

    def get_params(self):
        return {
            "user_ids": self.username
        }

    def response_handler(self, response):
        self.json_data = response.json()
        return self.json_data["response"][0]["uid"]

    def get_json(self):
        return self.json_data


class ClientGetFriendsAges(base_client.BaseClient):
    # метод vk api
    method = "friends"
    # GET, POST, ...
    http_method = "get"

    def __init__(self, user_id):
        self.user_id = user_id
        self.json_data = None

    def get_params(self):
        return {
            "user_id": self.user_id,
            "fields": "bdate"
        }

    def calculate_age(self, born, today):
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def response_handler(self, response):
        self.json_data = response.json()
        ages = list()
        today = datetime.utcnow()
        print("0-дата рождения не указана или она неполная")
        for friend in self.json_data["response"]:
            date_tmp = friend.get("bdate")
            if date_tmp is None or len(date_tmp) < 6:
                ages.append(self.calculate_age( datetime.strptime( "12.10.2017", "%d.%m.%Y"), today))
                continue
            ages.append( self.calculate_age( datetime.strptime( date_tmp, "%d.%m.%Y"), today))
        return ages

    def get_json(self):
        return self.json_data
