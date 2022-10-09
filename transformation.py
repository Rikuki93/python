from abc import ABC, abstractmethod


class Transformation(ABC):
    @abstractmethod
    def transform(self, data):
        pass
