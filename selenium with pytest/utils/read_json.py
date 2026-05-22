import json


def get_test_data():
    with open("test_data/beauty_test_data.json", "r") as file:
        data = json.load(file)

    return data