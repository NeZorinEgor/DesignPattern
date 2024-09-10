import uuid
from abc import ABC, abstractmethod


class ABCNomenclature(ABC):
    def __init__(self):
        self.__uuid = self.generate_uuid()

    @staticmethod
    def generate_uuid():
        return str(uuid.uuid4())

    @property
    def uuid(self):
        return self.__uuid

    @abstractmethod
    def local_eq(self, other):
        pass

    def __eq__(self, other):
        return self.uuid == other.uuid or self.local_eq(self)
