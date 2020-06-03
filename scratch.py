import json


class Vector:
    def __init__(self):
        self.x = x
        self.y = y


def my_decode(o):
    return o["copyright"]


with open("dictionary.json") as file:
    x = json.load(file, object_hook=my_decode)
    print(x)
