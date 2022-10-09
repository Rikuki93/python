from repository import Repository
from db import data
from transformation import Transformation


class JSONRepository(Repository):
    def __init__(self, transformation_service: Transformation):
        self.transformation_service = transformation_service

    def fetch_data(self):
        fetched_data = data
        return self.transformation_service.transform(data=fetched_data)
