import json
import os

from models.airplane import Airplane
from src.abstractFileHandler import AbstractFileHandler


class JsonFileHandler(AbstractFileHandler):
    def __init__(self, file_path: str):
        super().__init__(file_path)

    def save(self, airplanes: list[Airplane]):
        with open(self.path, 'w') as f:
            json.dump([airplane.to_dict() for airplane in airplanes], f)

    def load(self, airplanes: list[Airplane]):
        if not os.path.exists(self.path):
            raise FileNotFoundError('Файл не существует')

        with open(self.path, 'r') as f:
            data = json.load(f)

            return [Airplane.from_dict(plane) for plane in data]
