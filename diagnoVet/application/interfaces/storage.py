from abc import ABC, abstractmethod

class FileStorage(ABC):
    @abstractmethod
    def upload_pdf(self, path: str, content: bytes) -> str:
        pass