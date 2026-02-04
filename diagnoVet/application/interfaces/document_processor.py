from abc import ABC, abstractmethod


class DocumentProcessor(ABC):
    @abstractmethod
    
    def extract(self, content: bytes) -> str:
        pass