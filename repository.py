from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def fetch_data(self):
        pass
