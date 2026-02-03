from abc import ABC, abstractmethod

class Repository(ABC):

    @abstractmethod
    def save(self, report):
        pass

    @abstractmethod
    def get_by_id(self, report_id: str):
        pass