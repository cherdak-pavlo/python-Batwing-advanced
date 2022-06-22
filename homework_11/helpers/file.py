import json
from config import Config


def get_users():
    with open(Config.file_path, "r") as file:
        file_data = json.loads(file.read())
        return file_data


def write_users(users):
    with open(Config.file_path, "w") as file:
        file.write(json.dumps(users))
