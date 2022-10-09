from float_transformation import FloatTransformation
from json_repository import JSONRepository
from json_transformation import JSONTransformation
from repository import Repository
from string_transformation import StringTransformation


class ServiceGetData:
    def __init__(self, repository: Repository):
        self.repository = repository

    def get_data(self):
        return self.repository.fetch_data()


if __name__ == '__main__':
    transformation_service = JSONTransformation()
    repository = JSONRepository(transformation_service=transformation_service)
    service = ServiceGetData(repository=repository)
    print(service.get_data())

    transformation_service = StringTransformation()
    repository = JSONRepository(transformation_service=transformation_service)
    service = ServiceGetData(repository=repository)
    print(service.get_data())

    transformation_service = FloatTransformation()
    repository = JSONRepository(transformation_service=transformation_service)
    service = ServiceGetData(repository=repository)
    print(service.get_data())
