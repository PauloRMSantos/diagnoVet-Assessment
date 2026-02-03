from abc import ABC, abstractmethod


class DocumentProcessor(ABC):
    @abstractmethod
    def process(self, gcs_uri: str):
        pass