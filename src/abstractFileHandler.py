from abc import ABC, abstractmethod

from models.airplane import Airplane


class AbstractFileHandler(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def save(self, airplanes: list[Airplane]):
        pass

    @abstractmethod
    def load(self, airplanes: list[Airplane]):
        pass


