import json
import string


with open('utility/config.json', 'r') as config_file:
    data = json.load(config_file)


class config():
    @staticmethod
    def get(key: string):
        return data[key]
