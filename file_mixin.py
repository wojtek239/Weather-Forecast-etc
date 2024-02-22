import json


class FileMixin:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return None

    def write_to_file(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file)
